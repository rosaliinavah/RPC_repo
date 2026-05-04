# Python Style Guide for ATE Repository

This style guide defines the coding standards for Python development in the ATE repository, based on the established patterns in the codebase and pylint configuration.

## Table of Contents

1. [Naming Conventions](#naming-conventions)
2. [Code Structure](#code-structure)
3. [Documentation](#documentation)
4. [Type Hints](#type-hints)
5. [Error Handling](#error-handling)
6. [Formatting](#formatting)
7. [Design Constraints](#design-constraints)
8. [Robot Framework Integration](#robot-framework-integration)

---

## Naming Conventions

### General Rules

- **Classes**: Use `snake_case` for all class names
  ```python
  class ssh_connection_config:
      pass

  class command_result:
      pass
  ```

- **Functions and Methods**: Use `snake_case`
  ```python
  def configure_connection(self, address: str, username: str):
      pass

  def execute_command(self, command: str, timeout: int = 0):
      pass
  ```

- **Variables and Attributes**: Use `snake_case`
  ```python
  ssh_client = None
  execution_time = 0.0
  connection_config = None
  ```

- **Constants**: Use `UPPER_CASE` for class and module-level constants
  ```python
  ROBOT_LIBRARY_SCOPE: str = "GLOBAL"
  IO_TIMEOUT: float = 1.0
  CONNECTION_TIMEOUT: float = 1.0
  ```

- **Private Members**: Prefix with single underscore
  ```python
  def _connect(self):
      pass

  def _disconnect(self):
      pass

  self._connection_config = None
  self._connected = False
  ```

### Prohibited Names

Avoid these generic variable names: `foo`, `bar`, `baz`, `toto`, `tutu`, `tata`

### Acceptable Short Names

These single-letter or short names are acceptable:
- Loop counters: `i`, `j`, `k`
- Exception variables: `ex`, `e`
- Throwaway variables: `_`

---

## Code Structure

### Import Organization

Group imports in the following order with blank line separation:

1. Standard library imports
2. Third-party library imports
3. Local application imports

```python
import socket
import time
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Optional, Iterator

import paramiko

from robot.api import logger
```

### Class Organization

Structure classes with clear separation:

1. Class-level constants
2. `__init__` method
3. Public methods (Robot Framework keywords)
4. Private methods (helper functions)
5. Special methods (`__del__`, etc.)

Use section comments to delineate boundaries:

```python
class ssh:
    # Class constants
    ROBOT_LIBRARY_SCOPE: str = "GLOBAL"
    IO_TIMEOUT: float = 1.0

    def __init__(self):
        """Initialize instance."""
        pass

    # =========================================================================
    # PUBLIC ROBOT FRAMEWORK KEYWORDS
    # =========================================================================

    def configure_connection(self, address: str):
        """Public method."""
        pass

    # =========================================================================
    # PRIVATE METHODS
    # =========================================================================

    def _connect(self) -> None:
        """Private helper method."""
        pass
```

### Data Classes

Use `@dataclass` decorator for data containers:

```python
from dataclasses import dataclass

@dataclass
class command_result:
    """Store the result of executing a command."""
    command: str
    exit_code: int
    stdout: str
    stderr: str
    execution_time: float
```

---

## Documentation

### Module Docstrings

Every module must have a docstring at the top:

```python
"""Simplified SSH Client for Robot Framework test automation.

Focused on core SSH functionality for embedded device testing.
"""
```

### Class Docstrings

All classes require comprehensive docstrings:

```python
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
```

### Method Docstrings

Public methods must include:
- Brief description
- Args section with parameter descriptions
- Returns section (if applicable)
- Raises section (if applicable)
- Examples section with Robot Framework usage examples

```python
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
    """
```

### Private Method Docstrings

Private methods should have concise docstrings:

```python
def _connect(self) -> None:
    """Establish SSH connection using configured parameters.

    Creates and configures Paramiko SSH client, attempts authentication using either
    password or passwordless methods, and establishes transport connection to remote server.
    Handles both password and key-based authentication automatically.

    Raises:
    - `ssh_error`: If connection fails due to network, authentication, or configuration issues
    """
```

### Inline Comments

Use inline comments sparingly, only when logic isn't self-evident:

```python
# Use configured timeout if no specific timeout provided
effective_timeout = timeout if timeout > 0 else self._connection_config.timeout

# Try 'none' authentication for embedded devices
client = self._try_none_auth(cfg)
```

---

## Type Hints

### Mandatory Type Hints

All function/method signatures must include type hints:

```python
def configure_connection(self, address: str, username: str, password: str = "",
                         port: int = 22, timeout: int = 30) -> None:
    pass

def execute_command(self, command: str, timeout: int = 0) -> command_result:
    pass
```

### Standard Type Annotations

Use `typing` module for complex types:

```python
from typing import Optional, Iterator

self.ssh_client: Optional[paramiko.SSHClient] = None

@contextmanager
def _ensure_connection(self) -> Iterator[paramiko.SSHClient]:
    pass

def _collect_command_output(self, channel, timeout: int, start_time: float) -> tuple[list[str], list[str]]:
    pass
```

---

## Error Handling

### Custom Exceptions

Create domain-specific exceptions:

```python
class ssh_error(Exception):
    """Custom exception for SSH operation failures.

    Primary error type for all SSH-related failures, providing consistent interface for
    error handling. Wraps various underlying exceptions with descriptive messages.
    """
```

### Exception Chaining

Always chain exceptions with `from e`:

```python
try:
    client.connect(hostname=cfg.address, port=cfg.port)
except (OSError, IOError, TimeoutError) as e:
    self._connected = False
    raise ssh_error(f"Connection failed: {e}") from e
```

### Specific Exception Handling

Catch specific exceptions, avoid bare `except`:

```python
# Good
try:
    channel.exec_command(command)
except (OSError, IOError, paramiko.SSHException) as e:
    raise ssh_error(f"Failed to execute command: {e}") from e

# Acceptable only in cleanup code
def __del__(self):
    try:
        self._disconnect()
    except Exception:  # pylint: disable=broad-except
        pass
```

### Error Messages

Provide descriptive error messages with context:

```python
raise ssh_error(
    f"SSH connection test failed after {total_attempts} attempts: {last_exception}") from last_exception

raise ssh_error(
    f"TCP connection timed out after {ssh.CONNECTION_TIMEOUT}s: {cfg.address}:{cfg.port}") from e
```

---

## Formatting

### Line Length

- **Maximum**: 150 characters
- URLs and long strings can exceed this limit

```python
# This is acceptable if needed for readability
logger.info(
    f"SSH configured for {address}:{port} (Password enabled: {password_enabled})")
```

### Indentation

- Use **4 spaces** (not tabs)
- Continuation lines should indent 4 spaces

```python
self._connection_config = ssh_connection_config(
    address=address,
    username=username,
    password=password,
    port=port,
    timeout=timeout
)
```

### String Formatting

Use f-strings for string interpolation:

```python
# Good
logger.info(f"SSH connected to {cfg.address}:{cfg.port}")
message = f"Command completed in {execution_time:.2f}s with exit code {exit_code}"

# Avoid
message = "Command completed in {}s with exit code {}".format(execution_time, exit_code)
```

### Blank Lines

- Two blank lines between top-level class and function definitions
- One blank line between methods
- Logical sections within methods can be separated by blank lines

---

## Design Constraints

### Function/Method Complexity

Adhere to these limits (enforced by pylint):

- **Max arguments**: 10
- **Max local variables**: 15
- **Max statements**: 50
- **Max branches**: 12
- **Max returns**: 6
- **Max nested blocks**: 5

If you exceed these, refactor into smaller functions:

```python
# Refactored to reduce complexity
def _execute_on_client(self, client: paramiko.SSHClient, command: str,
                       timeout: int, start_time: float) -> command_result:
    # ...
    # Split the main loop logic to reduce complexity
    stdout_data, stderr_data = self._collect_command_output(
        channel, timeout, start_time)
    # ...
```

### Class Complexity

- **Max attributes**: 7
- **Max public methods**: 20
- **Max parents**: 7

---

## Robot Framework Integration

### Library Scope

Declare the library scope as a class constant:

```python
class ssh:
    ROBOT_LIBRARY_SCOPE: str = "GLOBAL"
```

### Keyword Documentation

Public methods are automatically Robot Framework keywords. Document with examples:

```python
def test_connection(self, timeout: int = 0, retry_count: int = 0) -> None:
    """Test if SSH connection can be established with current configuration.

    Attempts to connect and run simple test command (echo 'test'). Retries up to
    retry_count times if connection fails. Uses configured connection timeout when timeout=0.

    Args:
    - `timeout`: Connection timeout in seconds for each attempt (default: 0, uses configured timeout)
    - `retry_count`: Number of retry attempts if connection fails (default: 0, means 1 attempt total)

    Examples:
    | Configure Connection | 192.168.1.100 | user | pass |
    | Test Connection |
    | Test Connection | timeout=5 | retry_count=3 |
    """
```

### Logging

Use `robot.api.logger` for logging within Robot Framework context:

```python
from robot.api import logger

logger.info(f"SSH connected to {cfg.address}:{cfg.port}")
logger.warn(f"Connection test failed (attempt {attempt+1}/{total_attempts}): {e}")
logger.error(f"Command failed: {result.stderr}")
logger.debug(f"Command result: {command_result}")
```

---

## Additional Best Practices

### Context Managers

Use context managers for resource management:

```python
@contextmanager
def _ensure_connection(self) -> Iterator[paramiko.SSHClient]:
    """Ensure active SSH connection using context manager pattern."""
    try:
        self._connect()
        yield self.ssh_client
    except (OSError, IOError, paramiko.SSHException) as e:
        self._connected = False
        raise ssh_error(e) from e
    finally:
        self._disconnect()
```

### Boolean Checks

Convert values to boolean explicitly when needed:

```python
password_enabled = bool(password)
```

### Resource Cleanup

Implement `__del__` for cleanup when necessary:

```python
def __del__(self):
    """Clean up resources when object is destroyed."""
    try:
        self._disconnect()
    except Exception:  # pylint: disable=broad-except
        pass
```

### Pylint Directives

Use pylint directives only when necessary and document why:

```python
# Accessing protected member is necessary for none auth case
client._transport = transport  # pylint: disable=protected-access
```

---

## Pylint Configuration Summary

This repository uses pylint with the following key settings:

- Python version: 3.10+
- Naming: snake_case for classes, functions, methods, variables
- Max line length: 150
- Max module lines: 6000
- Docparams plugin enabled for parameter documentation checking
- Init hook adds "python_libs" to sys.path

For full configuration details, see [.pylintrc](.pylintrc).
