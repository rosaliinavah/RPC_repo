# Serial Connection Library for Robot Framework

This streamlined library provides serial communication capabilities with continuous logging, intelligent filtering, and simplified API for embedded device testing.

## 🚀 Key Features

- **Unified Connection Management**: Single method creates and starts connection automatically
- **Continuous Logging**: Comprehensive logging to Robot Framework logs and dedicated files
- **Smart Command Execution**: Unified method handles both response waiting and pattern matching
- **Intelligent Response Filtering**: Automatic command echo and prompt filtering
- **Flexible Prompt Detection**: Customizable regex patterns for shell prompt recognition
- **Robust Buffer Management**: Automatic size management with overflow protection
- **Thread-Safe Operations**: Safe concurrent access to connection resources
- **Simplified API**: Fewer methods, easier to learn and use

## 📋 Requirements

- **Python**: 3.6 or higher
- **Dependencies**:
  - `pyserial` - Serial port communication
  - `robotframework` - Test automation framework

## 🔧 Installation

### Option 1: Direct Installation
```bash
pip install pyserial robotframework
```

### Option 2: Requirements File
Create a `requirements.txt` file:
```
pyserial>=3.5
robotframework>=4.0
```

Then install:
```bash
pip install -r requirements.txt
```

### Option 3: Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pyserial robotframework
```

## 🛠️ Basic Usage

### Robot Framework Test Suite Example

```robotframework
*** Settings ***
Library             libraries/serial_con.py
Suite Setup         Setup Serial Connection
Suite Teardown      Cleanup Serial Connection

*** Variables ***
${DEVICE_PORT}     /dev/ttyUSB0
${BAUD_RATE}        115200
${TIMEOUT}         10.0

*** Test Cases ***
Device Boot Verification
    [Documentation]    Verify device boots successfully and reaches login prompt
    [Tags]    boot    critical

    # Wait for boot messages and login prompt
    ${boot_response}=    Wait For Pattern    .*login:.*    timeout=30
    Should Contain    ${boot_response}    login:
    Log    Device boot completed successfully

Basic Command Execution
    [Documentation]    Execute basic system commands and verify responses
    [Tags]    commands    smoke

    # Login and execute commands
    ${response}=    Send Command    root    timeout=5
    ${hostname}=    Send Command    hostname    timeout=3
    Should Not Be Empty    ${hostname}
    Log    Device hostname: ${hostname}

System Information Gathering
    [Documentation]    Collect system information for test reporting
    [Tags]    info    data-collection

    ${kernel_info}=    Send Command    uname -a    timeout=5
    ${memory_info}=    Send Command    free -h    timeout=5
    ${disk_info}=    Send Command    df -h    timeout=5

    Log    Kernel: ${kernel_info}
    Log    Memory: ${memory_info}
    Log    Disk: ${disk_info}

Pattern Matching Example
    [Documentation]    Demonstrate pattern matching for specific outputs
    [Tags]    patterns    advanced

    # Look for specific network interface using pattern parameter
    ${eth_interface}=    Send Command
    ...    ifconfig
    ...    timeout=10
    ...    pattern=eth0.*UP.*RUNNING
    Should Contain    ${eth_interface}    UP
    Should Contain    ${eth_interface}    RUNNING

*** Keywords ***
Setup Serial Connection
    [Documentation]    Initialize serial connection with optimal settings
    Connect
    ...    port=${DEVICE_PORT}
    ...    baud_rate=${BAUD_RATE}
    ...    log_path=logs/device_serial.log
    ...    timeout=0.5
    ...    term_char=\\r\\n
    ...    encoding=utf-8
    ...    buffer_size=500

    # Configure common prompt patterns for embedded Linux
    @{prompt_patterns}=    Create List
    ...    .*#\\s*$        # Root prompt
    ...    .*\\$\\s*$       # User prompt
    ...    .*>\\s*$        # Some shell prompts
    ...    .*login:\\s*$   # Login prompt
    Set Prompt Patterns    ${prompt_patterns}

    Log    Serial connection established on ${DEVICE_PORT}

Cleanup Serial Connection
    [Documentation]    Clean shutdown of serial connection
    Run Keyword If    ${True}    Disconnect
    Log    Serial connection closed
```

## 📚 Comprehensive Keyword Reference

### Connection Management

#### `Connect`
Creates, configures, and automatically starts the serial port connection.

**Parameters:**
- `port` (str): Serial port path (`/dev/ttyUSB0`, `COM3`, etc.)
- `baud_rate` (int, default=115200): Communication speed
- `log_path` (str, default="serial.log"): Path for continuous logging
- `timeout` (float, default=0.1): Read/write timeout in seconds
- `term_char` (str, default="\\n"): Line terminator (supports escape sequences)
- `encoding` (str, default="utf-8"): Character encoding
- `buffer_size` (int, default=500): Maximum buffered response lines

**Example:**
```robotframework
Connect    port=/dev/ttyUSB0    baud_rate=9600    timeout=1.0    term_char=\\r\\n
```

#### `Disconnect`
Stops the connection and releases all resources.

#### `Is Connection Active`
Returns boolean indicating if connection is active and running.

### Data Communication

#### `Write Data`
Sends raw data to the serial port.

**Parameters:**
- `data` (str): Data to send (supports escape sequences)

**Example:**
```robotframework
Write Data    hello world\\r\\n
```

#### `Send Command`
The primary method for command execution with unified response and pattern handling.

**Parameters:**
- `command` (str): Command to execute
- `timeout` (float, default=10.0): Maximum wait time
- `pattern` (str, default=""): Optional regex pattern to wait for
- `clear_buffer` (bool, default=True): Clear buffer before sending
- `filter_echo` (bool, default=True): Remove command echo from response

**Response Mode (default):**
```robotframework
# Wait for complete response
${output}=    Send Command    ls -la    timeout=5
```

**Pattern Mode:**
```robotframework
# Wait for specific pattern
${result}=    Send Command    reboot    timeout=30    pattern=Ready.*
```

**Advanced Example:**
```robotframework
# Handle commands with long output
${large_output}=    Send Command
...    find /usr -name "*.so" | head -100
...    timeout=30
...    clear_buffer=True
...    filter_echo=True
```

### Pattern Matching

#### `Wait For Pattern`
Monitors incoming data for regex pattern without sending commands.

**Parameters:**
- `pattern` (str): Regex pattern to match
- `timeout` (float, default=10.0): Maximum wait time

**Use Cases:**
- Monitoring boot sequences
- Waiting for autonomous system messages
- Detecting error conditions

**Example:**
```robotframework
# Wait for IP address assignment
${ip_result}=    Wait For Pattern    .*inet\\s+\\d+\\.\\d+\\.\\d+\\.\\d+.*    timeout=20
```

### Prompt Management

#### `Set Prompt Patterns`
Configures regex patterns for prompt detection and filtering.

**Parameters:**
- `patterns` (List[str]): List of regex strings for prompts

**Common Embedded Linux Patterns:**
```robotframework
@{patterns}=    Create List
...    .*#\\s*$                    # Root shell
...    .*\\$\\s*$                   # User shell
...    .*login:\\s*$               # Login prompt
...    .*Password:\\s*$            # Password prompt
...    .*\\(yes/no\\)\\?\\s*$       # SSH confirmation
Set Prompt Patterns    ${patterns}
```

### Buffer Management

#### `Get Response Buffer`
Returns copy of all buffered response lines for analysis.

#### `Clear Response Buffer`
Clears all stored response data from buffer and queue.

**Debugging Example:**
```robotframework
# Capture all communication for debugging
${all_responses}=    Get Response Buffer
Log    Complete communication history: ${all_responses}
Clear Response Buffer    # Clean slate for next test phase
```

## 🔍 Advanced Usage Patterns

### Error Handling Strategy
```robotframework
*** Test Cases ***
Robust Command Execution
    [Documentation]    Demonstrate proper error handling

    TRY
        ${result}=    Send Command    risky_command    timeout=5
        Log    Command succeeded: ${result}
    EXCEPT    response_timeout_error    AS    ${error}
        Log    Command timed out, continuing with fallback    WARN
        ${result}=    Set Variable    TIMEOUT_FALLBACK
    EXCEPT    serial_con_error    AS    ${error}
        Log    Serial communication error: ${error}    ERROR
        Fatal Error    Cannot continue without serial communication
    END
```

### Configuration File Testing
```robotframework
*** Test Cases ***
Configuration Validation
    [Documentation]    Validate device configuration files

    # Read and validate network configuration
    ${net_config}=    Send Command    cat /etc/network/interfaces
    Should Contain    ${net_config}    auto eth0
    Should Contain    ${net_config}    iface eth0 inet dhcp

    # Validate service configurations using pattern matching
    ${services}=    Send Command
    ...    systemctl list-unit-files --state=enabled
    ...    pattern=.*enabled.*
    Should Contain    ${services}    ssh.service
```

### Firmware Update Workflow
```robotframework
*** Test Cases ***
Firmware Update Process
    [Documentation]    Complete firmware update with verification

    # Initiate firmware update
    Send Command    update_firmware /tmp/new_firmware.bin    timeout=5

    # Wait for update completion
    ${update_complete}=    Wait For Pattern    .*Update completed.*    timeout=300
    Should Contain    ${update_complete}    completed

    # Wait for automatic reboot
    ${boot_message}=    Wait For Pattern    .*Boot successful.*    timeout=120
    Should Contain    ${boot_message}    successful

    # Verify new firmware version
    ${version}=    Send Command    get_firmware_version    timeout=5
    Should Contain    ${version}    v2.1.0
```

## 🚨 Exception Handling

### Exception Hierarchy
- `serial_con_error` - Base exception for all library errors
- `response_timeout_error` - Response or pattern not received within timeout

### Exception Examples
```robotframework
*** Test Cases ***
Handle Communication Errors
    TRY
        ${result}=    Send Command    test_command    timeout=2
    EXCEPT    response_timeout_error
        Log    Device did not respond in time    WARN
        # Implement retry logic or alternative approach
    EXCEPT    serial_con_error    AS    ${error}
        Log    Serial communication failed: ${error}    ERROR
        # Handle hardware or configuration issues
    END
```

## 🔧 Troubleshooting Guide

### Common Issues and Solutions

**Issue: Connection timeouts**
```robotframework
# Solution: Increase timeout and verify port settings
Connect    port=/dev/ttyUSB0    timeout=1.0    # Increase from default 0.1
```

**Issue: Command echo not filtered**
```robotframework
# Solution: Verify prompt patterns are set correctly
Set Prompt Patterns    @{your_prompt_patterns}
${result}=    Send Command    command    filter_echo=True
```

**Issue: Buffer overflow with large responses**
```robotframework
# Solution: Increase buffer size or clear buffer more frequently
Connect    buffer_size=1000    # Increase from default 500
Clear Response Buffer    # Clear between large operations
```

**Issue: Pattern not matching**
```robotframework
# Solution: Test patterns and use case-insensitive matching
${result}=    Wait For Pattern    (?i)ready.*    timeout=10    # Case insensitive
```

**Issue: Missing responses**
```robotframework
# Solution: Check continuous logging for complete communication history
${all_data}=    Get Response Buffer
Log    All received data: ${all_data}
```

## 🎯 Best Practices

### 1. Connection Management
- Always use Suite Setup/Teardown for connection lifecycle
- Set appropriate timeouts for your device's response characteristics
- Configure prompt patterns before sending commands

### 2. Command Execution
- Use `clear_buffer=True` for independent command sequences
- Set realistic timeouts based on expected command duration
- Use pattern matching for commands with variable output timing

### 3. Error Handling
- Always wrap critical commands in TRY/EXCEPT blocks
- Use specific exception types for targeted error handling
- Implement retry logic for transient communication issues

### 4. Debugging
- Leverage continuous logging for communication analysis
- Use `Get Response Buffer` to capture complete interaction history
- Enable detailed logging paths for post-test analysis

## 📈 Performance Tips

- Use smaller buffer sizes (500-1000) for memory efficiency
- Clear buffers between test phases to prevent memory buildup
- Set appropriate timeouts to balance responsiveness and reliability
- Use pattern matching instead of polling for better performance