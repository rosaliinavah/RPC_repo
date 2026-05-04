"""Simplified SSH Client for Robot Framework test automation.

Focused on core SSH functionality for embedded device testing.
"""

import socket
import time
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Optional, Iterator
import paramiko
from robot.api import logger


@dataclass
class command_result:
    """Store the result of executing a command over SSH connection.

    This dataclass provides structured access to command execution details including timing
    information and both success and error outputs. Used as return type for command methods.

    Examples:
    | ${result}= | Execute Command | ls -la |
    | Should Be Equal As Integers | ${result.exit_code} | 0 |
    | Log | ${result.stdout} |
    """
    command: str
    exit_code: int
    stdout: str
    stderr: str
    execution_time: float


@dataclass
class ssh_connection_config:
    """Store all configuration parameters for SSH connection establishment.

    Consolidates SSH connection settings into a single object to simplify function signatures
    and improve code maintainability. Supports password and passwordless authentication.

    Examples:
    | # Password authentication
    | Configure Connection | 192.168.1.100 | user | password123 |
    | # Passwordless authentication
    | Configure Connection | 192.168.1.100 | user |
    """
    address: str
    username: str
    password: str = ""
    port: int = 22
    timeout: int = 30


class ssh_error(Exception):
    """Custom exception for SSH operation failures.

    Primary error type for all SSH-related failures, providing consistent interface for
    error handling. Wraps various underlying exceptions with descriptive messages.

    Examples:
    | Run Keyword And Expect Error | ssh_error* | Execute Command | invalid_cmd |
    """


class ssh:
    """SSH client library for Robot Framework-based test automation.

    Provides comprehensive interface for automating SSH connections and remote command execution,
    designed with embedded systems testing and asynchronous operation in mind. All methods can
    be used directly as Robot Framework keywords.

    Examples:
    | Library | ssh.py |
    | Configure Connection | 192.168.1.100 | user | password |
    | ${result}= | Execute Command | uptime |
    """

    ROBOT_LIBRARY_SCOPE: str = "GLOBAL"
    # How long channel.recv() waits for data.
    IO_TIMEOUT: float = 1.0
    # How long the initial connection can take.
    CONNECTION_TIMEOUT: float = 1.0
    # How long is slept, before next connection retry.
    CONNECTION_RETRY_INTERVAL_S: float = 1.0
    # How long is slept, before each output is read from SSH channel.
    OUTPUT_RECV_INTERVAL_S: float = 0.1

    def __init__(self):
        """Initialize new SSH class instance.

        Sets up internal state for connection management including connection status flags,
        and empty tracking dictionary. Does not attempt to connect during initialization.
        """
        self.ssh_client: Optional[paramiko.SSHClient] = None
        self._connection_config: Optional[ssh_connection_config] = None
        self._connected: bool = False
        self._configured: bool = False

    # =========================================================================
    # PUBLIC ROBOT FRAMEWORK KEYWORDS
    # =========================================================================

    def configure_connection(self, address: str, username: str, password: str = "",
                             port: int = 22, timeout: int = 30) -> None:
        """Configure parameters for SSH connection establishment.

        Sets up SSH connection parameters for use with subsequent connection operations.
        Must be called before attempting to execute commands or test connections.

        Args:
        - `address`: SSH server IP address or hostname
        - `username`: SSH username for authentication
        - `password`: SSH password (leave empty for passwordless auth, default: "")
        - `port`: SSH server port number (default: 22)
        - `timeout`: Connection timeout in seconds (default: 30)

        Examples:
        | Configure Connection | 192.168.1.100 | testuser | mypassword |
        | Configure Connection | server.local | user |              | port=2222 |
        | Configure Connection | 10.0.0.1     | root |              | timeout=60 |
        """
        self._disconnect()

        self._connection_config = ssh_connection_config(
            address=address,
            username=username,
            password=password,
            port=port,
            timeout=timeout
        )

        self._connected = False
        self._configured = True

        password_enabled = bool(password)
        logger.info(
            f"SSH configured for {address}:{port} (Password enabled: {password_enabled})")

    def execute_command(self, command: str, timeout: int = 0) -> command_result:
        """Execute command on remote server over SSH and wait for completion.

        Opens new session channel, sends command, and collects stdout and stderr.
        Enforces maximum runtime timeout. Command is forcibly terminated if it exceeds
        allowed time. Uses configured connection timeout as default if no timeout specified.

        Args:
        - `command`: Command to execute on remote server
        - `timeout`: Maximum seconds to allow command to run (default: 0, uses configured timeout)

        Returns:
        - `command_result` object with command, exit code, output, error, and execution time

        Raises:
        - `ssh_error`: If command execution fails, times out, or connection not configured

        Examples:
        | ${result}= | Execute Command | ls -la |
        | Should Be Equal As Integers | ${result.exit_code} | 0 |
        | ${result}= | Execute Command | find / -name "*.log" | timeout=60 |
        | ${result}= | Execute Command | cat largefile.txt | timeout=10 |
        """
        if not self._configured:
            raise ssh_error(
                "SSH not configured. Use 'Configure Connection' first.")

        # Use configured timeout if no specific timeout provided
        effective_timeout = timeout if timeout > 0 else self._connection_config.timeout

        start_time = time.time()

        try:
            with self._ensure_connection() as client:
                return self._execute_on_client(client, command, effective_timeout, start_time)
        except (OSError, IOError, paramiko.SSHException) as e:
            elapsed = time.time() - start_time
            raise ssh_error(
                f"Command execution failed after {elapsed:.2f}s: {e}") from e

    def test_connection(self, timeout: int = 0, retry_count: int = 0) -> None:
        """Test if SSH connection can be established with current configuration.

        Attempts to connect and run simple test command (echo 'test'). Retries up to
        retry_count times if connection fails. Uses configured connection timeout when timeout=0.

        Args:
        - `timeout`: Connection timeout in seconds for each attempt (default: 0, uses configured timeout)
        - `retry_count`: Number of retry attempts if connection fails (default: 0, means 1 attempt total)

        Returns:
        - Success message if SSH connection and test command succeed

        Raises:
        - `ssh_error`: If connection cannot be established after all retry attempts

        Examples:
        | Configure Connection | 192.168.1.100 | user | pass |
        | Test Connection |
        | Test Connection | timeout=5 | retry_count=3 |  # 1 initial + 3 retries = 4 total attempts
        """
        if not self._configured:
            raise ssh_error(
                "SSH not configured. Use 'Configure Connection' first.")

        if retry_count < 0:
            raise ssh_error(
                "Negative retry_count given.")

        last_exception = None
        total_attempts = retry_count + 1  # Initial attempt + retries

        effective_timeout = timeout if timeout > 0 else self._connection_config.timeout

        for attempt in range(total_attempts):
            try:
                result = self.execute_command("echo 'test'", effective_timeout)
                if result.exit_code == 0 and "test" in result.stdout:
                    message = f"SSH connection successful to {self._connection_config.address}"
                    logger.info(message)
                    return

            except ssh_error as e:
                last_exception = e
                logger.warn(
                    f"Connection test failed (attempt {attempt+1}/{total_attempts}): {e}")
                if attempt < total_attempts - 1:  # Don't sleep after the last attempt
                    time.sleep(ssh.CONNECTION_RETRY_INTERVAL_S)

        # If we get here, all attempts failed
        raise ssh_error(
            f"SSH connection test failed: {last_exception}") from last_exception
    # =========================================================================
    # PRIVATE METHODS
    # =========================================================================

    @contextmanager
    def _ensure_connection(self) -> Iterator[paramiko.SSHClient]:
        """Ensure active SSH connection using context manager pattern.

        Establishes new connection if none exists, or reconnects if connection lost.
        Yields internal SSH client object for use within context and handles reconnection
        automatically if connection is dropped during operation.

        Returns:
        - Active SSH client instance for command execution

        Raises:
        - `ssh_error`: If connection parameters not set or reconnection fails

        Examples:
        | # Internal usage only - not a Robot Framework keyword
        | with self._ensure_connection() as client:
        |     # Use client for operations
        """
        try:
            self._connect()
            yield self.ssh_client
        except (OSError, IOError, paramiko.SSHException, TimeoutError, RuntimeError) as e:
            self._connected = False
            raise ssh_error(e) from e
        finally:
            self._disconnect()

    def _connect(self) -> None:
        """Establish SSH connection using configured parameters.

        Creates and configures Paramiko SSH client, attempts authentication using either
        password or passwordless methods, and establishes transport connection to remote server.
        Handles both password and key-based authentication automatically.

        Raises:
        - `ssh_error`: If connection fails due to network, authentication, or configuration issues

        Examples:
        | # Internal usage only - not a Robot Framework keyword
        | self._connect()  # Establishes connection using configured parameters
        """
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            cfg = self._connection_config

            if cfg.password:
                # Password authentication
                client.connect(
                    hostname=cfg.address,
                    port=cfg.port,
                    username=cfg.username,
                    password=cfg.password,
                    timeout=ssh.CONNECTION_TIMEOUT,
                    look_for_keys=False,
                    allow_agent=False,
                    channel_timeout=ssh.IO_TIMEOUT,
                    banner_timeout=ssh.CONNECTION_TIMEOUT,
                    auth_timeout=ssh.CONNECTION_TIMEOUT
                )
            else:
                # Passwordless authentication
                try:
                    client.connect(
                        hostname=cfg.address,
                        port=cfg.port,
                        username=cfg.username,
                        timeout=ssh.CONNECTION_TIMEOUT,
                        look_for_keys=True,
                        allow_agent=True,
                        channel_timeout=ssh.IO_TIMEOUT,
                        banner_timeout=ssh.CONNECTION_TIMEOUT,
                        auth_timeout=ssh.CONNECTION_TIMEOUT
                    )
                except (paramiko.AuthenticationException, paramiko.SSHException):
                    # Try 'none' authentication for embedded devices
                    logger.info("Using NONE authentication.")
                    client.close()
                    client = self._try_none_auth(cfg)

            self.ssh_client = client
            self._connected = True
            logger.info(f"SSH connected to {cfg.address}:{cfg.port}")

        except (OSError, IOError, TimeoutError) as e:
            self._connected = False
            if self.ssh_client:
                self.ssh_client.close()
                self.ssh_client = None
            raise ssh_error(f"Connection failed: {e}") from e

    def _disconnect(self) -> str:
        """Close SSH connection and clean up all related resources.

        Closes SSH client connection and resets connection status flags.
        Safe to call multiple times or when not connected.

        Returns:
        - Status message indicating disconnect success or warnings

        Examples:
        | # Internal usage only - not a Robot Framework keyword
        | self._disconnect()  # Disconnects the current connection
        """
        try:
            if self.ssh_client:
                self.ssh_client.close()
                self.ssh_client = None
            self._connected = False

            message = "SSH disconnected"
            logger.info(message)
            return message
        except (OSError, IOError, paramiko.SSHException) as e:
            logger.warn(f"Error during disconnect: {e}")
            return f"Disconnect completed with warnings: {e}"

    def _try_none_auth(self, cfg: ssh_connection_config) -> paramiko.SSHClient:
        """Attempt 'none' authentication for passwordless access to embedded devices.

        Creates SSH transport with TCP timeout and attempts 'none' authentication method,
        which is commonly used by embedded devices that allow passwordless access.
        Fallback method when standard passwordless authentication fails.

        Args:
        - `cfg`: SSH connection configuration object with server details

        Returns:
        - Connected and authenticated SSH client instance

        Raises:
        - `ssh_error`: If 'none' authentication fails or transport cannot be established

        Examples:
        | # Internal usage only - not a Robot Framework keyword
        | client = self._try_none_auth(self._connection_config)
        """
        sock = None
        transport = None

        try:
            # Create socket with timeout for TCP connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(ssh.CONNECTION_TIMEOUT)  # TCP connection timeout

            # Connect to the server with timeout
            sock.connect((cfg.address, cfg.port))

            # Create transport using the connected socket
            transport = paramiko.Transport(sock)
            # SSH handshake timeout
            transport.start_client(timeout=cfg.timeout)

            try:
                transport.auth_none(cfg.username)
            except paramiko.BadAuthenticationType:
                pass  # Some servers allow none auth even if they say they don't

            if not transport.is_authenticated():
                raise ssh_error("Passwordless authentication failed")

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # This is necessary for the none auth case - we need to use the transport directly
            client._transport = transport  # pylint: disable=protected-access

            # Don't close the transport here since client is using it
            return client

        except (OSError, IOError, TimeoutError, socket.gaierror, paramiko.SSHException) as e:
            # Clean up on error
            if transport:
                transport.close()
            elif sock:
                sock.close()

            if isinstance(e, TimeoutError):
                raise ssh_error(
                    f"TCP connection timed out after {ssh.CONNECTION_TIMEOUT}s: {cfg.address}:{cfg.port}") from e
            if isinstance(e, socket.gaierror):
                raise ssh_error(
                    f"DNS resolution failed for {cfg.address}: {e}") from e
            raise ssh_error(f"None authentication failed: {e}") from e

    def _execute_on_client(self, client: paramiko.SSHClient, command: str,
                           timeout: int, start_time: float) -> command_result:
        """Execute command on SSH client and collect output until completion.

        Opens session channel, executes command, and gathers stdout and stderr data
        until completion or timeout. Handles I/O timeouts and enforces maximum runtime limits.
        Returns structured result with execution details.

        Args:
        - `client`: Active Paramiko SSHClient for opening session channel
        - `command`: Shell command to execute on remote host
        - `timeout`: Maximum seconds to allow command to run
        - `start_time`: Epoch timestamp marking command execution start

        Returns:
        - `command_result` instance with command, exit code, stdout, stderr, and execution time

        Raises:
        - `ssh_error`: If error opening session, executing command, or timeout occurs

        Examples:
        | # Internal usage only - not a Robot Framework keyword
        | result = self._execute_on_client(client, "ls -la", 30, time.time())
        """
        transport = client.get_transport()
        if not transport:
            raise ssh_error("SSH transport not available")

        try:
            channel = transport.open_session()
        except (OSError, IOError, paramiko.SSHException) as e:
            raise ssh_error(f"Failed to open session: {e}") from e

        channel.settimeout(ssh.IO_TIMEOUT)  # I/O timeout, channel.recv()

        try:
            channel.exec_command(command)
        except (OSError, IOError, paramiko.SSHException) as e:
            channel.close()
            raise ssh_error(f"Failed to execute command: {e}") from e

        # Split the main loop logic to reduce complexity
        stdout_data, stderr_data = self._collect_command_output(
            channel, timeout, start_time)

        exit_code = channel.recv_exit_status()
        execution_time = time.time() - start_time

        result = command_result(
            command=command,
            exit_code=exit_code,
            stdout=''.join(stdout_data).strip(),
            stderr=''.join(stderr_data).strip(),
            execution_time=execution_time
        )
        logger.debug(f"Command result: {command_result}")
        logger.debug(
            f"Command completed in {execution_time:.2f}s with exit code {exit_code}")
        if exit_code != 0:
            if not result.stderr:
                logger.error("Command timed out.")
            else:
                logger.error(f"Command failed: {result.stderr}")
            raise ssh_error(f"Command failed with exit code: {exit_code}")

        return result

    def _collect_command_output(self, channel, timeout: int, start_time: float) -> tuple[list[str], list[str]]:
        """Collect stdout and stderr from command execution channel.

        Helper method to reduce complexity in _execute_on_client.

        Args:
        - `channel`: SSH channel for command execution
        - `timeout`: Maximum seconds to allow command to run
        - `start_time`: Epoch timestamp marking command execution start

        Returns:
        - Tuple of (stdout_data, stderr_data) as lists of strings

        Raises:
        - `ssh_error`: If command times out
        """
        stdout_data = []
        stderr_data = []

        finalize: bool = False
        # Collect output until command completes or times out
        while True:
            # Read available stdout
            if channel.recv_ready():
                data = channel.recv(1024)
                if data:
                    stdout_data.append(data.decode('utf-8', errors='replace'))

            # Read available stderr
            if channel.recv_stderr_ready():
                data = channel.recv_stderr(1024)
                if data:
                    stderr_data.append(data.decode('utf-8', errors='replace'))

            # Check if command finished or timeout achieved
            if channel.exit_status_ready() or time.time() - start_time > timeout:
                # Ensure one more loop is run to get remaining data.
                if not finalize:
                    finalize = True
                    continue
                channel.close()
                break

            time.sleep(ssh.OUTPUT_RECV_INTERVAL_S)

        return stdout_data, stderr_data

    def __del__(self):
        """Clean up resources when SSH client object is destroyed.

        Attempts to disconnect and suppresses any exceptions during cleanup to prevent
        shutdown issues. Called automatically when object goes out of scope or is garbage collected.

        Examples:
        | # Internal usage only - automatically called during object destruction
        | del ssh_client  # Triggers __del__ method
        """
        try:
            self._disconnect()
        except Exception:  # pylint: disable=broad-except
            pass
