*** Settings ***
Documentation       Resource file for DUT related variables.

Resource            libraries_and_variables.resource
Resource            power_management.resource


*** Keywords ***
Unlock Device Under Test
    [Documentation]     Sends GFC message and writes password
    [Arguments]         ${node_id}    ${password}

    DeviceUnderTest_CAN1.Send Gfc Message
    BuiltIn.Sleep    0.5s

    ${status}  ${protection_status} =   Run Keyword And Ignore Error
    ...                                 DeviceUnderTest_CAN1.Read Protection Status         node_id=${node_id}
    IF  $status == 'FAIL'   BuiltIn.Fatal Error     msg=Device did not respond to SDO read

    BuiltIn.Should Be True    ${protection_status}[0] == 0 or ${protection_status}[0] == 170

    ${status} =                         Run Keyword And Ignore Error
    ...                                 DeviceUnderTest_CAN1.Write Controlunit Password     node_id=${node_id}  password=${password}
    IF  $status == 'FAIL'   BuiltIn.Fatal Error     msg=Device did not respond to SDO write

    ${status}  ${protection_status} =   Run Keyword And Ignore Error
    ...                                 DeviceUnderTest_CAN1.Read Protection Status         node_id=${node_id}
    IF  $status == 'FAIL'   BuiltIn.Fatal Error     msg=Device did not respond to SDO read

    ${passed} =                         BuiltIn.Run Keyword And Return Status
    ...                                 BuiltIn.Should Be True      ${protection_status}[0] == 170
    IF  not ${passed}       BuiltIn.Fatal Error     msg=Device password unlock was unsuccessful

Remove Application From DUT
    [Documentation]     Removes application from DUT.

    Unlock Device Under Test                        node_id=${FW_NODE_ID}   password=${PASSWORD}
    DeviceUnderTest_CAN1.Remove Application         node_id=${FW_NODE_ID}
    Power Cycle DUT And Wait For Bootup Message     node_id=${FW_NODE_ID}

Read Ethernet IP Address
    [Documentation]    Reads and returns DUT Ethernet IP address as separate octets.
    ...                For example, for IP 192.168.0.2 returns: 192.168.0.2
    [Arguments]         ${node_id}=${FW_NODE_ID}

    ${eth_ip_1} =        DeviceUnderTest_CAN1.Read Sdo    node_id=${node_id}    index_name=0x2141    sub_name=19
    ${eth_ip_2} =        DeviceUnderTest_CAN1.Read Sdo    node_id=${node_id}    index_name=0x2141    sub_name=20
    ${eth_ip_3} =        DeviceUnderTest_CAN1.Read Sdo    node_id=${node_id}    index_name=0x2141    sub_name=21
    ${eth_ip_4} =        DeviceUnderTest_CAN1.Read Sdo    node_id=${node_id}    index_name=0x2141    sub_name=22

    RETURN    ${eth_ip_1}.${eth_ip_2}.${eth_ip_3}.${eth_ip_4}

Write Ethernet IP Address
    [Documentation]     Writes DUT Ethernet IP address.
    ...                 IP address format: xxx.xxx.xxx.xxx (e.g. 192.168.0.2)
    [Arguments]         ${node_id}    ${ip_address}

    ${octets} =     String.Split String         ${ip_address}    .
    DeviceUnderTest_CAN1.Write Sdo    node_id=${node_id}    index_name=0x2141    sub_name=19    data=${octets}[0]
    DeviceUnderTest_CAN1.Write Sdo    node_id=${node_id}    index_name=0x2141    sub_name=20    data=${octets}[1]
    DeviceUnderTest_CAN1.Write Sdo    node_id=${node_id}    index_name=0x2141    sub_name=21    data=${octets}[2]
    DeviceUnderTest_CAN1.Write Sdo    node_id=${node_id}    index_name=0x2141    sub_name=22    data=${octets}[3]

Write CAN Bitrate And Application Node ID
    [Documentation]     Writes CAN bitrate and application node ID values.
    ...                 Writes values for specified CAN interface (1 or 2).
    ...
    ...                 Arguments:
    ...                 - can: CAN interface number 1=CAN1, 2=CAN2
    ...                 - bitrate: CAN bitrate to write
    ...                 - app_node_id: Application node ID to write
    [Arguments]         ${can}    ${bitrate}    ${app_node_id}

    DeviceUnderTest_CAN1.Write Sdo    node_id=${FW_NODE_ID}    index_name=0x215${${can}-1}    sub_name=3    data=${bitrate}
    DeviceUnderTest_CAN1.Write Sdo    node_id=${FW_NODE_ID}    index_name=0x215${${can}-1}    sub_name=10   data=${app_node_id}

Read CAN Bitrate And Application Node ID
    [Documentation]     Reads CAN bitrate and application node ID values.
    ...                 Reads values for specified CAN interface (1 or 2).
    ...
    ...                 Returns:
    ...                 - CAN bitrate
    ...                 - Application node ID
    [Arguments]         ${can}    ${node_id}

    ${bitrate} =    DeviceUnderTest_CAN1.Read Sdo   node_id=${node_id}    index_name=0x215${${can}-1}    sub_name=3
    ${app_node} =   DeviceUnderTest_CAN1.Read Sdo   node_id=${node_id}    index_name=0x215${${can}-1}    sub_name=10

    RETURN    ${bitrate}    ${app_node}

Execute Factory Reset
    [Documentation]    Executes Factory Reset for DUT.

    VAR    ${START_FACTORY_RESET_TIME}    12s
    VAR    ${FACTORY_RESET_ERASE_TIME}    30s

    Power Off DUT
    BuiltIn.Sleep    5s    reason=Wait for HW to completely power-off
    Set BSL/Wire Harness Id Pin Voltage            ${-9.5}
    BuiltIn.Sleep    200ms

    Power On DUT
    BuiltIn.Sleep  ${START_FACTORY_RESET_TIME}

    Set BSL/Wire Harness Id Pin Voltage            ${0}
    BuiltIn.Sleep  ${FACTORY_RESET_ERASE_TIME}

Set BSL/Wire Harness ID Pin Voltage
    [Documentation]     Set the voltage in BSL/Wire harness ID pin.
    ...                 - Allowed range with this keyword is -10..10V
    ...                 - Default 2.5V
    [Arguments]         ${value}=${2.5}

    VeristandApi.Write Channel Value        channel_name=${ALIASES_ATE_IO21_AO}        value=${value}

Set BSL/Wire Harness ID Pin Voltage To 24V
    [Documentation]     Set the voltage in BSL/Wire harness ID pin to 24V with ATE DO.
    ...                 True  : Set voltage to 24V
    ...                 False : Set voltage to current ATE AOU voltage
    [Arguments]         ${enable}

    IF  $enable
        VeristandApi.Write Channels Values
        ...    ${ALIASES_ATE_IO21_SELECT_DO_OR_AOR}    ${True}
        ...    ${ALIASES_ATE_IO21_PWM_DC}              ${100}
        ...    ${ALIASES_ATE_IO21_PWM_FR}              ${100}
    ELSE
        VeristandApi.Write Channels Values
        ...    ${ALIASES_ATE_IO21_PWM_DC}              ${0}
        ...    ${ALIASES_ATE_IO21_PWM_FR}              ${0}
        ...    ${ALIASES_ATE_IO21_SELECT_DO_OR_AOR}    ${False}
    END

Verify Password Type
    [Documentation]    Verifies password type by reading specific FW OD index value.
    [Arguments]        ${node_id}    ${expected_type}

    ${password_type} =    DeviceUnderTest_CAN1.Read Sdo    node_id=${node_id}    index_name=ProtectionStatus    sub_name=Password type
    BuiltIn.Should Be Equal As Integers    ${expected_type}    ${password_type}

Reset Password With PUK-code And Reboot Device
    [Documentation]    Unlocks device with PUK-code and resets password to default.
    ...
    ...                1. If special PUK-code is not defined, calculate default by using DUT S/N.
    ...                2. Unlock device with PUK-code and verify unlock status
    ...                3. Write default password to device and save all parameters

    VAR    ${UNLOCK_STATUS_UNLOCKED}    ${0xAA}
    # 1. If special PUK-code is not defined, calculate default by using DUT S/N.
    IF  not ${PUK_CODE}
        ${PUK_CODE} =    BitOperations.Calculate Puk Code From Serial Number    serial_number=${PLC_SERIAL_NUMBER}
    END

    # 2. Unlock device with PUK-code and verify unlock status
    DeviceUnderTest_CAN1.Send Gfc Message
    BuiltIn.Sleep    0.5s
    DeviceUnderTest_CAN1.Write Control Unit Puk Code    node_id=${FW_NODE_ID}      puk_code=${PUK_CODE}

    ${protection_status} =   DeviceUnderTest_CAN1.Read Protection Status    node_id=${FW_NODE_ID}
    ${passed} =  BuiltIn.Run Keyword And Return Status
    ...    BuiltIn.Should Be Equal As Integers              ${protection_status}[0]    ${UNLOCK_STATUS_UNLOCKED}
    IF    not ${passed}      BuiltIn.Fatal Error    msg=Device unlock failed with PUK-code: ${PUK_CODE}

    # 3. Write default password to device and save all parameters
    DeviceUnderTest_CAN1.Write Sdo Raw            node_id=${FW_NODE_ID}    index_name=0x2031    data=${PASSWORD}    sub_name=2
    DeviceUnderTest_CAN1.Save All Parameters      node_id=${FW_NODE_ID}

    Power Cycle DUT

Unlock Device And Change Password
    [Documentation]    Unlocks device with correct password, write new password and save all parameters.
    [Arguments]        ${node_id}    ${password}    ${new_password}

    Unlock Device Under Test                    node_id=${node_id}    password=${password}
    DeviceUnderTest_CAN1.Write Sdo Raw          node_id=${node_id}    index_name=0x2031    data=${new_password}    sub_name=2
    DeviceUnderTest_CAN1.Save All Parameters    node_id=${node_id}
