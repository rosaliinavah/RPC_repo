"""Streamlined Robot Framework Serial Logger Library.

Simplified serial communication library for Robot Framework with continuous logging,
response buffering, and pattern matching for embedded device testing. Provides a
clean, unified API for single connection management and intelligent response filtering.
"""

import logging
import pathlib
import queue
import re
import threading
import time
from typing import List, Optional, Pattern

import serial
import serial.tools.list_ports
from robot.api import logger as robot_logger
from robot.libraries.BuiltIn import BuiltIn


class serial_con_error(Exception):
    """Base exception for serial connection operations."""


class response_timeout_error(serial_con_error):
    """Raised when waiting for a response times out."""


class serial_con:
    """Robot Framework library for serial communication with continuous logging.

    Provides simplified methods to connect, send commands, and retrieve responses with
    automatic filtering and timeouts for embedded device testing. Library scope is
    GLOBAL to ensure single connection management across test cases.
    """

    ROBOT_LIBRARY_SCOPE: str = 'GLOBAL'

    def __init__(self) -> None:
        """Initialize the serial_con library with connection management.

        Sets up internal connection placeholder for operations.
        Connection must be created separately using connect().
        """
        self._connection: Optional[_serial_handler] = None

    # ============================================================================
    # PUBLIC METHODS - Robot Framework Keywords
    # ============================================================================

    def connect(
        self,
        port: str,
        baud_rate: int = 115200,
        *,
        log_path: str = "",
        timeout: float = 0.1,
        term_char: str = "\\n",
        encoding: str = "utf-8",
        buffer_size: int = 500
    ) -> None:
        """Create and start a serial connection with continuous logging.

        Args:
        - `port`: Serial port path (e.g., '/dev/ttyUSB0', 'COM3')
        - `baud_rate`: Communication speed (default: 115200)
        - `log_path`: Log file path (auto-generated if empty)
        - `timeout`: Read timeout in seconds (default: 0.1)
        - `term_char`: Line terminator (default: \\n)
        - `encoding`: Character encoding (default: utf-8)
        - `buffer_size`: Max buffered lines (default: 500)

        Raises:
        - `serial_con_error`: If connection already exists or port cannot be opened

        Examples:
        | Connect | /dev/ttyUSB0 |        | # Create with defaults
        | Connect | COM3         | 9600   | # Windows with 9600 baud
        """
        # Check if the given COM-port exists.
        # Warn the user if COM-port is missing and then raise an Exception.
        ports = [port.device for port in serial.tools.list_ports.comports()]
        if port not in ports:
            robot_logger.warn(
                f"{port} does not exist!\nAvailable ports: {', '.join(ports)}")
            raise serial_con_error(
                f"{port} does not exist."
            )
        if self._connection is not None:
            raise serial_con_error(
                "Connection already exists. Stop it first.")

        if not log_path:
            suite_name = serial_con.get_suite_name()
            log_path = f"{suite_name.lower().replace(' ', '_')}.log" if suite_name else "serial.log"

        try:
            term_char_bytes = term_char.encode().decode("unicode_escape").encode(encoding)
            self._connection = _serial_handler(
                port=port,
                baud_rate=baud_rate,
                log_path=log_path,
                timeout=timeout,
                term_char=term_char_bytes,
                encoding=encoding,
                buffer_size=buffer_size,
            )
            self._connection.start()
            robot_logger.info(
                f"Created and started serial connection on {port} @ {baud_rate} baud")
        except Exception as e:
            raise serial_con_error(
                f"Failed to Connect: {e}") from e

    def disconnect(self) -> None:
        """Stop the serial connection and release resources.

        Raises:
        - `serial_con_error`: If connection cannot be stopped properly

        Examples:
        | Disconnect | # Clean shutdown
        """
        if self._connection is None:
            return
        try:
            self._connection.stop()
            robot_logger.info("Stopped serial connection")
        except Exception as e:
            raise serial_con_error(
                f"Failed to disconnect: {e}") from e
        finally:
            self._connection = None

    def send_command(
        self,
        command: str,
        timeout: float = 10.0,
        *,
        pattern: str = "",
        clear_buffer: bool = True,
        filter_echo: bool = True
    ) -> str:
        """Send command and wait for response or pattern match.

        Args:
        - `command`: Command to send
        - `timeout`: Max wait time in seconds (default: 10.0)
        - `pattern`: Optional regex pattern to wait for (waits for complete response if empty)
        - `clear_buffer`: Clear buffer before sending (default: True)
        - `filter_echo`: Filter out command echo (default: True)

        Returns:
        - Device response or matched line

        Raises:
        - `serial_con_error`: If no connection exists or write operation fails
        - `response_timeout_error`: If response or pattern match times out

        Examples:
        | ${response}= | Send Command | help                    |      | # Wait for complete response
        | ${line}=     | Send Command | reboot | pattern=Ready.* | 30.0 | # Wait for specific pattern
        """
        conn = self._get_connection()
        if clear_buffer:
            conn.clear_buffer()

        conn.write(command + "\r\n")

        if pattern:
            return conn.wait_for_pattern(pattern, timeout)

        return conn.wait_for_response(timeout, command if filter_echo else None)

    def wait_for_pattern(
        self,
        pattern: str,
        timeout: float = 10.0
    ) -> str:
        """Wait for a regex pattern in the serial output.

        Args:
        - `pattern`: Regex pattern to match
        - `timeout`: Max wait time in seconds (default: 10.0)

        Returns:
        - First line matching the pattern

        Raises:
        - `serial_con_error`: If no connection exists or invalid regex pattern
        - `response_timeout_error`: If pattern is not found within timeout

        Examples:
        | ${event}= | Wait For Pattern | Temperature.*C | 30.0 |
        """
        return self._get_connection().wait_for_pattern(pattern, timeout)

    def write_data(self, data: str) -> None:
        """Write raw data to the serial connection.

        Args:
        - `data`: Data to send (supports escape sequences)

        Raises:
        - `serial_con_error`: If no connection exists or write operation fails

        Examples:
        | Write Data | hello\\r\\n | # Send with explicit line ending
        """
        processed = data.encode().decode("unicode_escape")
        self._get_connection().write(processed)

    def set_prompt_patterns(self, patterns: List[str]) -> None:
        """Set regex patterns for shell prompt filtering.

        Args:
        - `patterns`: List of regex strings for prompts

        Raises:
        - `serial_con_error`: If no connection exists or invalid regex patterns

        Examples:
        | Set Prompt Patterns | ["root@.*:.*#", "\\$ "] |
        """
        self._get_connection().set_prompt_patterns(patterns)

    def get_response_buffer(self) -> List[str]:
        """Return all buffered response lines.

        Returns:
        - List of all buffered response lines

        Raises:
        - `serial_con_error`: If no connection exists

        Examples:
        | @{buffer}= | Get Response Buffer |
        """
        return self._get_connection().get_buffer()

    def clear_response_buffer(self) -> None:
        """Clear all stored response lines.

        Raises:
        - `serial_con_error`: If no connection exists

        Examples:
        | Clear Response Buffer |
        """
        self._get_connection().clear_buffer()

    def is_connection_active(self) -> bool:
        """Check if connection is active.

        Returns:
        - True if connection exists and is running, False otherwise

        Examples:
        | ${active}= | Is Connection Active |
        """
        return bool(self._connection and self._connection.is_running())

    # ============================================================================
    # PRIVATE METHODS
    # ============================================================================

    def _get_connection(self) -> '_serial_handler':
        """Get active connection handler or raise error if none exists.

        Returns:
        - Active _serial_handler instance for operations

        Raises:
        - `serial_con_error`: If no connection exists

        Internal helper method that ensures connection exists before operations.
        """
        if not self._connection:
            raise serial_con_error(
                "No connection exists; call connect() first.")
        return self._connection

    @staticmethod
    def get_suite_name() -> str:
        """Get Robot Framework suite name for auto-generated log file names.

        Returns:
        - Current suite name or empty string if unavailable

        Used for automatic log file naming when log_path is not specified.
        """
        try:
            return BuiltIn().get_variable_value("${SUITE_NAME}", "")
        except Exception:  # pylint: disable=broad-except
            return ""

    @staticmethod
    def get_test_name() -> str:
        """Get Robot Framework suite name for auto-generated log file names.

        Returns:
        - Current test name or empty string if unavailable

        Used for automatic log file naming when log_path is not specified.
        """
        try:
            return BuiltIn().get_variable_value("${TEST_NAME}", "")
        except Exception:  # pylint: disable=broad-except
            return ""

    def __del__(self) -> None:
        """Destructor ensures clean connection shutdown during garbage collection.

        Automatically stops active connection when object is destroyed.
        Silently handles errors during interpreter shutdown.
        """
        try:
            self.disconnect()
        except Exception:  # pylint: disable=broad-except
            pass


class _serial_handler:  # pylint: disable=too-few-public-methods,too-many-instance-attributes
    """Internal serial port handler with continuous logging."""
    QUEUE_TIMEOUT: float = 0.05

    def __init__(
        self,
        port: str,
        baud_rate: int,
        *,
        log_path: str,
        timeout: float,
        term_char: bytes,
        encoding: str,
        buffer_size: int
    ) -> None:
        """Initialize serial handler with port configuration and logging setup.

        Args:
        - `port`: Serial port path (e.g., '/dev/ttyUSB0', 'COM3')
        - `baud_rate`: Communication speed in bits per second
        - `log_path`: File path for continuous logging
        - `timeout`: Read/write timeout in seconds
        - `term_char`: Line terminator as bytes
        - `encoding`: Character encoding for data conversion
        - `buffer_size`: Maximum number of lines to buffer

        Raises:
        - `serial_con_error`: If serial port cannot be opened
        """
        # Configuration parameters grouped together
        self.config = {
            'port': port,
            'baud_rate': baud_rate,
            'encoding': encoding,
            'term_char': term_char,
            'timeout': timeout
        }

        try:
            self.ser = serial.Serial(
                port=port,
                baudrate=baud_rate,
                timeout=timeout,
                write_timeout=timeout
            )
        except serial.SerialException as e:
            raise serial_con_error(f"Cannot open port {port}: {e}") from e

        # Lock for buffering
        self._buffer_lock = threading.Lock()

        # Threading and control grouped
        self._thread_ctrl = {
            'stop_event': threading.Event(),
            'reader_thread': None,
            'is_running': False
        }

        # Data management
        self._buffer: List[str] = []
        self._queue: queue.Queue[str] = queue.Queue(maxsize=buffer_size)
        self._prompt_patterns: List[Pattern[str]] = []

        # Logging
        self.file_logger = self._setup_logger(log_path)

    def _setup_logger(self, log_path: str) -> logging.Logger:
        """Setup file logger for continuous logging with timestamp formatting.

        Args:
        - `log_path`: File path for log output

        Returns:
        - Configured logger instance for serial communication logging
        """
        pathlib.Path(log_path).parent.mkdir(parents=True, exist_ok=True)
        logger = logging.getLogger(f"SerialLogger_{self.config['port']}")
        logger.handlers.clear()
        handler = logging.FileHandler(log_path, encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        return logger

    def start(self) -> None:
        """Start the connection and begin continuous logging.

        Opens serial port and starts background thread for data monitoring.
        Thread-safe operation that prevents multiple starts.

        Raises:
        - `serial_con_error`: If connection is already running
        """
        if self._thread_ctrl['is_running']:
            raise serial_con_error("Connection already running")

        if not self.ser.is_open:
            self.ser.open()

        self._thread_ctrl['stop_event'].clear()
        self._thread_ctrl['reader_thread'] = threading.Thread(
            target=self._reader_loop, daemon=True)
        self._thread_ctrl['is_running'] = True
        self.file_logger.info("Started on %s @ %s",
                              self.config['port'], self.config['baud_rate'])
        self._thread_ctrl['reader_thread'].start()

    def stop(self, timeout: float = 2.0) -> None:
        """Stop the connection and cleanup resources.

        Args:
        - `timeout`: Maximum time to wait for thread shutdown (default: 2.0)

        Stops background thread and closes serial port safely.
        """
        if not self._thread_ctrl['is_running']:
            return

        self._thread_ctrl['stop_event'].set()
        if self._thread_ctrl['reader_thread'] and self._thread_ctrl['reader_thread'].is_alive():
            self._thread_ctrl['reader_thread'].join(timeout)

        if self.ser.is_open:
            self.ser.close()

        self._thread_ctrl['is_running'] = False
        self.file_logger.info("Stopped on %s", self.config['port'])

    def write(self, data: str) -> None:
        """Write data to serial port with continuous logging.

        Args:
        - `data`: String data to send to device

        Raises:
        - `serial_con_error`: If connection is not running or write operation fails

        Encodes data and sends to serial port while logging transmission.
        """
        if not self._thread_ctrl['is_running']:
            raise serial_con_error("Connection not running")

        try:
            encoded = data.encode(self.config['encoding'])
            self.ser.write(encoded)
            self.ser.flush()
            display = data.replace("\r", "\\r").replace("\n", "\\n")
            test_info = serial_con.get_suite_name() + "." + serial_con.get_test_name()
            self.file_logger.info("[%s] TX: %s", test_info, display)
            robot_logger.info(f"TX: {display}")
        except Exception as e:
            raise serial_con_error(f"Write failed: {e}") from e

    def wait_for_response(
        self,
        timeout: float,
        filter_command: Optional[str] = None
    ) -> str:
        """Wait for complete response with command echo and prompt filtering.

        Args:
        - `timeout`: Maximum wait time in seconds
        - `filter_command`: Command string to filter from echo (default: None)

        Returns:
        - Filtered response text as joined lines

        Raises:
        - `response_timeout_error`: If no response is received within timeout
        """
        end_time = time.time() + timeout
        lines: List[str] = []
        command_filtered = not filter_command

        while time.time() < end_time:
            try:
                line = self._queue.get(timeout=_serial_handler.QUEUE_TIMEOUT)

                # Filter command echo
                if not command_filtered and filter_command:
                    if self._is_command_echo(line, filter_command):
                        command_filtered = True
                        continue

                # Filter prompts
                if self._is_prompt_line(line):
                    continue

                lines.append(line)

                # Brief pause to collect any additional lines
                time.sleep(_serial_handler.QUEUE_TIMEOUT)
                while time.time() < end_time:
                    try:
                        additional = self._queue.get_nowait()
                        if not self._is_prompt_line(additional):
                            lines.append(additional)
                    except queue.Empty:
                        break
                break

            except queue.Empty:
                continue

        if not lines:
            raise response_timeout_error(f"No response within {timeout}s")

        return "\n".join(lines).strip()

    def wait_for_pattern(self, pattern: str, timeout: float) -> str:
        """Wait for regex pattern match in incoming data.

        Args:
        - `pattern`: Regex pattern to search for
        - `timeout`: Maximum wait time in seconds

        Returns:
        - First line matching the pattern

        Raises:
        - `serial_con_error`: If regex pattern is invalid
        - `response_timeout_error`: If pattern is not found within timeout
        """
        try:
            regex = re.compile(pattern, re.IGNORECASE)
        except re.error as e:
            raise serial_con_error(f"Invalid regex '{pattern}': {e}") from e

        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                line = self._queue.get(timeout=_serial_handler.QUEUE_TIMEOUT)
                if regex.search(line):
                    return line
            except queue.Empty:
                continue

        raise response_timeout_error(
            f"Pattern '{pattern}' not found within {timeout}s")

    def set_prompt_patterns(self, patterns: List[str]) -> None:
        """Set regex patterns for prompt filtering.

        Args:
        - `patterns`: List of regex strings to identify device prompts

        Raises:
        - `serial_con_error`: If any regex pattern is invalid

        Compiles patterns and validates regex syntax before storage.
        """
        compiled = []
        for pattern in patterns:
            try:
                compiled.append(re.compile(pattern))
            except re.error as e:
                raise serial_con_error(
                    f"Invalid pattern '{pattern}': {e}") from e
        with self._buffer_lock:
            self._prompt_patterns = compiled

    def get_buffer(self) -> List[str]:
        """Get copy of response buffer for analysis.

        Returns:
        - Copy of all buffered response lines
        """
        with self._buffer_lock:
            return self._buffer.copy()

    def clear_buffer(self) -> None:
        """Clear response buffer and queue to free memory.

        Removes all stored response data from buffer and queue.
        """
        with self._buffer_lock:
            self._buffer.clear()

        while not self._queue.empty():
            try:
                self._queue.get_nowait()
            except queue.Empty:
                break

    def is_running(self) -> bool:
        """Check if connection is active and monitoring data.

        Returns:
        - True if connection is running and port is open
        """
        return self._thread_ctrl['is_running'] and self.ser.is_open

    def _reader_loop(self) -> None:
        """Continuous reading and logging loop for background thread.

        Monitors serial port for incoming data and processes complete lines.
        Runs until stop event is set.
        """
        buffer = bytearray()

        while not self._thread_ctrl['stop_event'].wait(0.01):
            try:
                if self.ser.in_waiting:
                    data = self.ser.read(self.ser.in_waiting)
                    buffer.extend(data)
                    self._process_lines(buffer)
            except (serial.SerialException, UnicodeDecodeError) as e:
                if not self._thread_ctrl['stop_event'].is_set():
                    self.file_logger.error("Read error: %s", e)
                    robot_logger.error("Read error: %s", e)
                break

    def _process_lines(self, buffer: bytearray) -> None:
        """Extract complete lines from incoming data buffer.

        Args:
        - `buffer`: Mutable byte buffer containing incoming serial data

        Splits on term_char delimiter and logs each complete line.
        """
        while self.config['term_char'] in buffer:
            line_bytes, _, rest = buffer.partition(self.config['term_char'])
            buffer[:] = rest

            line = line_bytes.decode(
                self.config['encoding'], errors="replace").rstrip()
            if line:
                test_info = serial_con.get_suite_name() + "." + serial_con.get_test_name()
                self.file_logger.info("[%s] RX: %s", test_info, line)
                robot_logger.info(f"RX: {line}")
                self._store_line(line)

    def _store_line(self, line: str) -> None:
        """Store received line in buffer and queue with size management.

        Args:
        - `line`: Complete line of text from device

        Adds line to both buffer and queue with automatic size limits.
        """
        with self._buffer_lock:
            self._buffer.append(line)
            # Keep buffer reasonable size
            if len(self._buffer) > 1000:
                self._buffer = self._buffer[-500:]

        try:
            self._queue.put_nowait(line)
        except queue.Full:
            try:
                self._queue.get_nowait()  # Remove oldest
                self._queue.put_nowait(line)
            except queue.Empty:
                pass

    def _is_command_echo(self, line: str, command: str) -> bool:
        """Check if received line is echo of sent command.

        Args:
        - `line`: Received line from device
        - `command`: Originally sent command string

        Returns:
        - True if line matches command after prompt removal
        """
        clean_line = line.strip()

        # Remove prompt prefix if present
        for pattern in self._prompt_patterns:
            match = pattern.match(clean_line)
            if match:
                clean_line = clean_line[match.end():].strip()
                break

        return clean_line == command.strip()

    def _is_prompt_line(self, line: str) -> bool:
        """Check if line matches configured prompt patterns.

        Args:
        - `line`: Received line to test against prompt patterns

        Returns:
        - True if line matches any configured prompt regex
        """
        with self._buffer_lock:
            return any(pattern.match(line.rstrip()) for pattern in self._prompt_patterns)
