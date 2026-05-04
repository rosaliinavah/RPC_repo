# Simplified SSH & SFTP Libraries for Robot Framework

Streamlined Python libraries providing **SSH** and **SFTP** functionality designed specifically for Robot Framework test automation of embedded Linux devices.

## 🎯 Key Features

### SSH Client (`ssh.py`)
* **Simple command execution** with structured results
* **Password and passwordless authentication** (including 'none' auth for embedded devices)
* **Automatic connection management** with context managers
* **Configurable timeout and retry support**
* **Structured error handling** with custom exceptions

### SFTP Client (`sftp.py`)
* **Smart transfer detection** - single `Upload To Remote`/`Download From Remote` keywords handle both files and directories
* **Secure file transfers** with optional integrity verification
* **Automatic directory creation** and recursive operations
* **Built-in file size validation** and transfer verification
* **Inherits all SSH functionality** - can execute commands and manage SSH connections

---

## 🧠 Smart Transfer Detection

The `Upload To Remote` and `Download From Remote` keywords automatically detect whether you're transferring a file or directory:

### How it Works

**Upload Detection:**
- Checks if local path is a file → uploads single file
- Checks if local path is a directory → uploads entire directory recursively
- Creates remote directories as needed

**Download Detection:**
- Checks if remote path is a file → downloads single file
- Checks if remote path is a directory → downloads entire directory recursively
- Creates local directories as needed

### Benefits
- **Simplified API**: One keyword handles both scenarios
- **Less cognitive load**: No need to remember separate keywords
- **Error prevention**: Automatic validation of path types
- **Optional verification**: Built-in integrity checking via file size comparison

```robotframework
# Unified keywords handle both files and directories automatically
Upload To Remote    firmware.bin    /tmp/firmware.bin     # Auto-detects file
Upload To Remote    config/         /etc/myapp/           # Auto-detects directory
Download From Remote  /var/log/app.log     app.log        # Auto-detects file
Download From Remote  /var/log/myapp/      backup_logs/   # Auto-detects directory
```

---

## 📦 Installation

```bash
pip install paramiko robotframework
```

Place `ssh.py` and `sftp.py` in your Robot Framework library path.

---

## 📋 Data Structures

### `command_result`
```python
@dataclass
class command_result:
    command: str           # The executed command
    exit_code: int         # Exit status (0 = success)
    stdout: str           # Standard output
    stderr: str           # Standard error
    execution_time: float # Execution time in seconds
```

### `ssh_connection_config`
```python
@dataclass
class ssh_connection_config:
    address: str           # Hostname/IP
    username: str          # SSH username
    password: str = ""     # Password (optional for passwordless)
    port: int = 22         # SSH port
    timeout: int = 30      # Connection timeout
```

---

## 🚀 Quick Start Examples

### Basic SSH Usage

**Robot Framework:**
```robotframework
*** Settings ***
Library    ssh.py

*** Variables ***
${HOST}      192.168.1.100
${USER}      admin
${PASSWORD}  secret123

*** Test Cases ***
Execute Basic Commands
    Configure Connection    ${HOST}    ${USER}    ${PASSWORD}
    Test Connection

    ${result}=    Execute Command    uptime
    Should Be Equal As Integers    ${result.exit_code}    0
    Log    System uptime: ${result.stdout}

    ${result}=    Execute Command    df -h
    Should Contain    ${result.stdout}    /
```

**Python:**
```python
from ssh import ssh

cli = ssh()
cli.configure_connection("192.168.1.100", "admin", "secret123")

result = cli.execute_command("uname -a")
print(f"Exit code: {result.exit_code}")
print(f"Output: {result.stdout}")
```

### Basic SFTP Usage

**Robot Framework:**
```robotframework
*** Settings ***
Library    sftp.py

*** Test Cases ***
File Transfer Test
    Configure Connection    ${HOST}    ${USER}    ${PASSWORD}
    Test Connection

    # Upload single file (with automatic verification)
    Upload To Remote    config.txt    /tmp/config.txt

    # Upload entire directory
    Upload To Remote    test_data/    /tmp/test_data/

    # Download single file
    Download From Remote    /tmp/config.txt    downloaded_config.txt

    # Download entire directory
    Download From Remote    /var/log/myapp/    local_logs/

    # Upload without verification (faster for large files)
    Upload To Remote    large_file.bin    /tmp/large_file.bin    verify=False

    # Cleanup
    Remove From Remote    /tmp/config.txt

Download Latest Modified File From Remote Directory
    Configure Connection    ${HOST}    ${USER}    ${PASSWORD}

    # Download and rename file (with automatic verification)
    Download Latest File From Remote    /home/lvuser/logs-archive    local_dir/measurement_file.tdms

    # Download file with the same name as source file (without automatic verification)
    Download Latest File From Remote    /home/lvuser/logs-archive    verify=False

List All Files In Remote Directory
    Configure Connection    ${HOST}    ${USER}    ${PASSWORD}

    # Each file in the list is tuple (File name, file size, modified date/time)
    ${files}= List Files In Remote Directory   /home/lvuser/logs-archive

Smart Transfer Detection
    Configure Connection    ${HOST}    ${USER}    ${PASSWORD}

    # The same keyword works for both files and directories
    Upload To Remote    firmware.bin         /tmp/firmware.bin      # Detected as file
    Upload To Remote    config_folder/       /etc/myapp/            # Detected as directory

    Download From Remote  /var/log/app.log     app.log              # Detected as file
    Download From Remote  /var/log/myapp/      backup_logs/         # Detected as directory

Combined SSH and SFTP Operations
    Configure Connection    ${HOST}    ${USER}    ${PASSWORD}

    # Upload firmware
    Upload To Remote    firmware.bin    /tmp/firmware.bin

    # Execute commands (SFTP inherits SSH functionality)
    ${result}=    Execute Command    chmod +x /tmp/firmware.bin
    Should Be Equal As Integers    ${result.exit_code}    0

    # Install firmware
    ${result}=    Execute Command    /tmp/firmware.bin --install
    Should Be Equal As Integers    ${result.exit_code}    0

    # Download logs
    Download From Remote    /var/log/install.log    install.log
```

**Python:**
```python
from sftp import sftp

fs = sftp()
fs.configure_connection("192.168.1.100", "admin", "secret123")

# Upload file or directory - automatically detected
fs.upload_to_remote("local_file.txt", "/tmp/remote_file.txt")          # File upload
fs.upload_to_remote("local_folder/", "/tmp/remote_folder/")            # Directory upload

# Execute commands (SFTP inherits SSH functionality)
result = fs.execute_command("ls -la /tmp/")
print(f"Directory listing: {result.stdout}")

# Download file or directory - automatically detected
fs.download_from_remote("/tmp/remote_file.txt", "downloaded_file.txt")   # File download
fs.download_from_remote("/tmp/remote_folder/", "downloaded_folder/")     # Directory download
```

### Passwordless Authentication

```robotframework
*** Test Cases ***
Passwordless Connection
    # No password parameter for passwordless auth
    Configure Connection    ${HOST}    ${USER}
    Test Connection

    ${result}=    Execute Command    whoami
    Should Be Equal    ${result.stdout.strip()}    ${USER}

Embedded Device None Auth
    # Many embedded devices support 'none' authentication
    Configure Connection    ${EMBEDDED_HOST}    root
    Test Connection

    ${result}=    Execute Command    cat /proc/version
    Should Contain    ${result.stdout}    Linux
```

---

## 📖 API Reference

### SSH Keywords

| Keyword | Purpose | Arguments |
|---------|---------|-----------|
| `Configure Connection` | Set connection parameters | address, username, password="", port=22, timeout=30 |
| `Execute Command` | Run command on remote host | command, timeout=0 |
| `Test Connection` | Test connection with retry | timeout=0, retry_count=0 |

**Notes:**
- When `timeout=0` in `Execute Command`, uses the configured connection timeout
- Failed commands (non-zero exit codes) raise `ssh_error` exceptions
- `retry_count=0` means 1 total attempt (no retries)

### SFTP Keywords

**Note:** SFTP library inherits from SSH, so all SSH keywords are also available.

| Keyword | Purpose | Arguments |
|---------|---------|-----------|
| `Test Connection` | Test SFTP capability | timeout=10, retry_count=0 |
| `Upload To Remote` | Upload file or directory to remote | local_path, remote_path, verify=True |
| `Download From Remote` | Download file or directory from remote | remote_path, local_path, verify=True |
| `Download Latest File From Remote` | Download latest modified file from remote directory | remote_dir, local_path, verify=True |
| `List Files In Remote Directory` | Lists all files in remote directory | remote_dir |
| `Remove From Remote` | Delete remote file/directory | remote_path |

**Notes:**
- `verify=True` enables automatic file size verification after transfer
- Verification compares file sizes (not checksums) between local and remote
- Progress logging occurs every 10 files for directory operations
- `retry_count=0` means 1 total attempt (no retries)

---

## 🔧 Common Patterns

### Error Handling
```robotframework
*** Test Cases ***
Handle Command Errors
    Configure Connection    ${HOST}    ${USER}    ${PASSWORD}

    # This will raise ssh_error for non-zero exit codes
    Run Keyword And Expect Error    ssh_error*    Execute Command    invalid_command

    # For commands that may legitimately fail, catch the exception
    ${status}    ${result}=    Run Keyword And Return Status    Execute Command    test -f /nonexistent
    Should Be False    ${status}
```

### Performance Considerations
```robotframework
*** Test Cases ***
Large File Transfer
    Configure Connection    ${HOST}    ${USER}    ${PASSWORD}

    # Disable verification for large files to improve speed
    Upload To Remote    large_database.sql    /tmp/large_database.sql    verify=False

    # Use longer timeout for slow commands
    ${result}=    Execute Command    md5sum /tmp/large_database.sql    timeout=300
    Log    Checksum: ${result.stdout}

Firmware Deployment Test
    Configure Connection    ${HOST}    ${USER}    ${PASSWORD}

    # Upload firmware and config
    Upload To Remote    firmware.bin           /tmp/firmware.bin
    Upload To Remote    device_config/         /etc/device/

    # Execute deployment (using inherited SSH functionality)
    ${result}=    Execute Command    /tmp/firmware.bin --install    timeout=120
    Should Be Equal As Integers    ${result.exit_code}    0

    # Download logs with verification enabled
    Download From Remote    /var/log/install.log    install.log    verify=True
```

### Connection Testing
```robotframework
*** Test Cases ***
Test Device Connectivity
    Configure Connection    ${HOST}    ${USER}    ${PASSWORD}

    # Test with retries for unreliable networks
    Test Connection    timeout=15    retry_count=3

    Log    Device is accessible via SSH and SFTP
```

---

## 🛡️ Security Notes

- **Path validation**: Basic protection against directory traversal attacks
- **Authentication**: Supports password, key-based, and 'none' authentication
- **Connection management**: Automatic cleanup and reconnection handling
- **Error handling**: Consistent error reporting through custom exception classes
- **Verification**: Optional integrity checking via file size comparison

---

## 🔍 Troubleshooting

### Common Issues

1. **Connection timeout**: Increase timeout parameter or check network connectivity
2. **Authentication failed**: Verify credentials or SSH key setup for passwordless auth
3. **File not found**: Check paths and permissions on both local and remote systems
4. **Transfer integrity failure**: Network issues, insufficient disk space, or file corruption
5. **Command timeout**: Commands with `timeout=0` use connection timeout, increase if needed

### Debug Tips

- Use `Test Connection` with retries to verify basic connectivity
- Check Robot Framework logs for detailed error messages
- Verify file permissions and disk space on target device
- For passwordless auth, ensure SSH keys are properly configured or try 'none' auth
- Use `Execute Command` with SFTP library to run diagnostic commands
- Disable verification (`verify=False`) for large files to improve performance
- Increase timeouts for slow networks or large operations

### Known Limitations

- File integrity verification only compares sizes, not checksums
- Directory verification only checks local→remote, not for extra remote files
- Failed file downloads in directories are logged as warnings but don't stop the process
- Progress logging is hardcoded to every 10 files

---

## 🗃️ Library Architecture

### Inheritance Structure
```
ssh (base class)
└── sftp (inherits from ssh)
```

The SFTP library extends the SSH library, meaning:
- All SSH keywords are available when using the SFTP library
- Connection management is shared between SSH and SFTP operations
- You can mix SSH commands and SFTP file operations in the same test

### Exception Hierarchy
```
ssh_error (base exception)
└── sftp_error (inherits from ssh_error)
```

Both libraries use consistent error handling patterns for easier debugging.

### Connection Management
- Connections are established on-demand and cleaned up automatically
- Context managers ensure proper resource cleanup
- Supports multiple authentication methods including embedded device 'none' auth
- Automatic retry and timeout handling

---

This implementation focuses on core functionality needed for embedded device testing while maintaining the Robot Framework keyword interface and providing comprehensive file transfer capabilities with optional verification.