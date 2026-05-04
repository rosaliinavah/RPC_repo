*** Settings ***
Documentation       Main resource file for ATE test environment.

Resource            resources/libraries_and_variables.resource
Resource            resources/power_management.resource
Resource            resources/can_management.resource
Resource            resources/artifact.resource
Resource            resources/dut.resource
Resource            resources/common.resource


*** Keywords ***
Setup Bench
    [Documentation]    Keyword for Suite setup to make sure bench is set OK

    XnetDbUtility.Register Xnet Databases

    BuiltIn.Wait Until Keyword Succeeds    3 times    500ms
    ...    Veristand Stop, Start And Deploy

    AliasXmlParser.Compare Aliases Files
    ...    veristand_folder=${VERISTAND_PATH}
    ...    robot_resource_file_path=${VERISTAND_SYSTEM_ALIASES_RESOURCE_PATH}

    DeviceUnderTest_CAN1.Connect    bustype=${CAN1_BUSTYPE}       channel=${CAN1_CHANNEL}          bitrate=${CAN1_BITRATE}
    DeviceUnderTest_CAN3.Connect    bustype=${CAN3_BUSTYPE}       channel=${CAN3_CHANNEL}          bitrate=${CAN3_BITRATE}

    DeviceUnderTest_CAN1.Add Node   node_id=${FW_NODE_ID}         eds_file_path=${FW_EDS_FILE}
    DeviceUnderTest_CAN1.Add Node   node_id=${APP_NODE_ID}        eds_file_path=${SYSTEM_APP_EDS_FILE}
    DeviceUnderTest_CAN3.Add Node   node_id=${CAN3_APP_NODE_ID}   eds_file_path=${SYSTEM_APP_CAN3_EDS_FILE}

    VeristandApi.Write Channel Value            channel_name=${ALIASES_ATE_POWER_ENABLE_4}    value=1
    Power On DUT

    # TODO: Needs to be more dynamic to know when device is booted
    BuiltIn.Sleep    5s

    Verify DUT Hardware Revision And Device Name

    Enable All ATE CAN Ports

    Set ATE Pin Default Values And Reset DUT Pin Diagnostic

Teardown Bench
    [Documentation]    Keyword for Suite setup to make sure bench is shut down OK

    Add Firmware Metadata To Report
    Add Application Metadata To Report
    Add EDS Metadata To Report    metadata_file_path=${PATH_TO_CAN1_EDS_METADATA}    eds_file_path=${SYSTEM_APP_EDS_FILE}
    Add EDS Metadata To Report    metadata_file_path=${PATH_TO_CAN3_EDS_METADATA}    eds_file_path=${SYSTEM_APP_CAN3_EDS_FILE}

    XnetDbUtility.Unregister Xnet Databases
    DeviceUnderTest_CAN1.Disconnect
    DeviceUnderTest_CAN3.Disconnect

    Power Off DUT
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_POWER_ENABLE_4}    value=0

    VeristandApi.Disconnect System And Undeploy Definition
    VeristandApi.Stop    timeout_s=${VERISTAND_STOP_TIMEOUT_S}

Setup Test
    [Documentation]    Keyword to setup test

    Set Global Variable  ${TESTCASE_INDEX}  ${TESTCASE_INDEX+1}

    VeristandApi.Write Channel Value  channel_name=${ALIASES_ROBOT_TESTCASE_INDEX}    value=${TESTCASE_INDEX}

    DeviceUnderTest_CAN1.Nmt Set Operational
    DeviceUnderTest_CAN3.Nmt Set Operational
    BuiltIn.Sleep    0.1s

Teardown Test
    [Documentation]    Keyword to teardown test

    IF  $TEST_STATUS == 'FAIL'
        ${error_logs} =    BuiltIn.Run Keyword And Warn On Failure
        ...    DeviceUnderTest_CAN1.Get Firmware Error Log Latest 25
        ...    fw_node_id=${FW_NODE_ID}
        BuiltIn.Log    ${error_logs}
    END

    Check Veristand Alarms

Verify DUT Hardware Revision And Device Name
    [Documentation]    Reads detailed version info from DUT.
    ...                Verifies HW revision and device name.

    ${detailed_info} =  DeviceUnderTest_CAN1.Get Detailed Version Info       node_id=${FW_NODE_ID}

    ${passed} =    BuiltIn.Run Keyword And Return Status
    ...    BuiltIn.Should Contain
    ...    container=${detailed_info}
    ...    item=HW:${PLC_HW_REVISION}
    IF    not ${passed}      BuiltIn.Fatal Error    msg=Wrong DUT in test bench, hardware version mismatch!

    ${passed} =    BuiltIn.Run Keyword And Return Status
    ...    BuiltIn.Should Contain
    ...    container=${detailed_info}
    ...    item=Codesys device name:${PLC_DEVICE_NAME}
    IF    not ${passed}      BuiltIn.Fatal Error    msg=Wrong DUT in test bench, device name mismatch!

Check Veristand Alarms
    [Documentation]    Checks alarms from Veristand and stops execution if fault alarms are ON.

    ${status} =    BuiltIn.Run Keyword And Return Status    VeristandApi.Check Alarms

    IF    not ${status}
        BuiltIn.Fatal Error    msg=Alarms are ON, Test Execution needs to stop!
    END

Add Firmware Metadata To Report
    [Documentation]    Fetches Firmware related information from DUT and adds them to Metadata if not already fetched.

    OperatingSystem.Remove File     path=${PATH_TO_FW_METADATA}
    ${status}    ${detailed_info} =    BuiltIn.Run Keyword And Ignore Error
    ...    DeviceUnderTest_CAN1.Get Detailed Version Info
    ...    node_id=${FW_NODE_ID}

    IF    $status == 'PASS'
        ${build_nbr} =    OperatingSystem.Get Environment Variable
        ...    name=RESOURCES_PIPELINE_FW_RUNNAME
        ...    default=Local
        @{detailed_info_array} =    String.Split String    string=${detailed_info}    separator=\n
        OperatingSystem.Append To File
        ...    path=${PATH_TO_FW_METADATA}
        ...    content=Build nbr: ${build_nbr}\n\n
        ...    encoding=UTF-8

        FOR    ${item}  IN  @{detailed_info_array}
            OperatingSystem.Append To File
            ...    path=${PATH_TO_FW_METADATA}
            ...    content=${item}\n\n
            ...    encoding=UTF-8
        END
    END

Add Application Metadata To Report
    [Documentation]    Fetches Application related information from DUT and adds them to Metadata

    OperatingSystem.Remove File     path=${PATH_TO_APP_METADATA}

    ${status}    ${error} =    BuiltIn.Run Keyword And Ignore Error
    ...    DeviceUnderTest_CAN1.Get Device Type    ${APP_NODE_ID}
    IF    $status == 'PASS'
        ${software_information} =    DeviceUnderTest_CAN1.Read Sdo
        ...    node_id=${APP_NODE_ID}
        ...    index_name=SoftwareInformation
        ...    sub_name=1
        OperatingSystem.Append To File
        ...    path=${PATH_TO_APP_METADATA}
        ...    content=MTC project: ${software_information}\n\n
        ...    encoding=UTF-8

        ${software_information} =    DeviceUnderTest_CAN1.Read Sdo
        ...    node_id=${APP_NODE_ID}
        ...    index_name=SoftwareInformation
        ...    sub_name=2
        ${content} =    String.Split String    string=${software_information}    separator=\x00
        OperatingSystem.Append To File
        ...    path=${PATH_TO_APP_METADATA}
        ...    content=Codesys project: ${content}[0]\n\n
        ...    encoding=UTF-8

        ${software_information} =    DeviceUnderTest_CAN1.Read Sdo
        ...    node_id=${APP_NODE_ID}
        ...    index_name=SoftwareInformation
        ...    sub_name=3
        ${content} =    String.Split String    string=${software_information}    separator=\x00
        OperatingSystem.Append To File
        ...    path=${PATH_TO_APP_METADATA}
        ...    content=Application title: ${content}[0]\n\n
        ...    encoding=UTF-8

        ${software_information} =    DeviceUnderTest_CAN1.Read Sdo
        ...    node_id=${APP_NODE_ID}
        ...    index_name=SoftwareInformation
        ...    sub_name=4
        ${content} =    String.Split String    string=${software_information}    separator=\x00
        OperatingSystem.Append To File
        ...    path=${PATH_TO_APP_METADATA}
        ...    content=Application version: ${content}[0]\n\n
        ...    encoding=UTF-8

        ${software_information} =    DeviceUnderTest_CAN1.Read Sdo
        ...    node_id=${APP_NODE_ID}
        ...    index_name=SoftwareInformation
        ...    sub_name=5
        ${content} =    String.Split String    string=${software_information}    separator=\x00
        OperatingSystem.Append To File
        ...    path=${PATH_TO_APP_METADATA}
        ...    content=Device: ${content}[0]\n\n
        ...    encoding=UTF-8

        ${software_information} =    DeviceUnderTest_CAN1.Read Sdo
        ...    node_id=${APP_NODE_ID}
        ...    index_name=SoftwareInformation
        ...    sub_name=6
        ${content} =    String.Split String    string=${software_information}    separator=\x00
        OperatingSystem.Append To File
        ...    path=${PATH_TO_APP_METADATA}
        ...    content=Device version: ${content}[0]\n\n
        ...    encoding=UTF-8
    ELSE
        OperatingSystem.Append To File
        ...    path=${PATH_TO_APP_METADATA}
        ...    content=${error}\n\n
        ...    encoding=UTF-8
    END

Add EDS Metadata To Report
    [Documentation]    Fetches information from EDS file and adds them to Metadata.
    [Arguments]        ${metadata_file_path}    ${eds_file_path}

    OperatingSystem.Remove File     path=${metadata_file_path}

    ${eds_file_content} =   OperatingSystem.Get File    path=${eds_file_path}     encoding=UTF-8
    @{eds_file_array} =     String.Split To Lines       string=${eds_file_content}

    OperatingSystem.Append To File
    ...    path=${metadata_file_path}
    ...    content=${eds_file_array[5]}\n\n
    ...    encoding=UTF-8

    OperatingSystem.Append To File
    ...    path=${metadata_file_path}
    ...    content=${eds_file_array[6]}\n\n
    ...    encoding=UTF-8

    OperatingSystem.Append To File
    ...    path=${metadata_file_path}
    ...    content=${eds_file_array[7]}\n\n
    ...    encoding=UTF-8

    OperatingSystem.Append To File
    ...    path=${metadata_file_path}
    ...    content=${eds_file_array[9]}\n\n
    ...    encoding=UTF-8

    OperatingSystem.Append To File
    ...    path=${metadata_file_path}
    ...    content=${eds_file_array[10]}\n\n
    ...    encoding=UTF-8

Veristand Stop, Start And Deploy
    [Documentation]    Keyword to make sure NI Veristand is up and running and deployed.

    VeristandApi.Stop       timeout_s=${VERISTAND_STOP_TIMEOUT_S}
    VeristandApi.Start      timeout_s=${VERISTAND_START_TIMEOUT_S}
    VeristandApi.Connect To System And Deploy Definition
    ...    sdf_path=${VERISTAND_SDF_PATH_SYSTEM}
    ...    deploy=${True}
    ...    timeout_s=${VERISTAND_SDF_DEPLOY_TIMEOUT_S}

Power Cycle DUT And Disable/Enable ATE CAN
    [Documentation]    Disable ATE CAN, Power cycle DUT and wait for boot up message. Enable ATE CAN.
    [Arguments]        ${node_id}

    Disable All ATE CAN Ports

    Power Cycle DUT And Wait For Bootup Message    ${node_id}

    Enable All ATE CAN Ports

Setup Application
    [Documentation]     Updates application and verifies version from DUT.

    Download Application To DUT    ${FW_NODE_ID}    ${APP_NODE_ID}    ${SYSTEM_APP_BIN_FILE}
    Check Application Version Information
    # Probably not needed, because this is done already in Setup Bench
    # Set ATE Pin Default Values And Reset DUT Pin Diagnostic

Download Application To DUT
    [Documentation]     Downloads application to DUT.
    [Arguments]         ${fw_node_id}    ${app_node_id}    ${app_bin_path}

    Unlock Device Under Test    node_id=${fw_node_id}    password=${PASSWORD}

    DeviceUnderTest_CAN1.Download Application    node_id=${fw_node_id}    app_bin_path=${app_bin_path}

    Power Cycle DUT And Wait For Bootup Message    ${app_node_id}      timeout=60

Check Application Version Information
    [Documentation]    Reads version information from application with APP node-ID.
    [Arguments]        ${node_id}=${APP_NODE_ID}

    ${dut_app_version} =    DeviceUnderTest_CAN1.Read Sdo
    ...    node_id=${node_id}
    ...    index_name=SoftwareInformation
    ...    sub_name=4

    ${app_version} =    Read APP Version From Artifact Info File    info_file=${SYSTEM_APP_INFO_FILE}
    BuiltIn.Should Contain
    ...    container=${dut_app_version}
    ...    item=${app_version}

Set ATE Pin Default Values And Reset DUT Pin Diagnostic
    [Documentation]   Sets default values for ATE output pins and resets DUT pin diagnostic to clear possible fault state

    # Suite 10 pins
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO62_AO}    value=2.5
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO63_AO}    value=0.01

    # Suite 11 pins
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO57_AO}    value=2.5
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO58_AO}    value=0.01

    # Suite 13 pins
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO43_AO}    value=2.5
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO46_AO}    value=2.5
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO47_AO}    value=0.01

    # Suite 14 pins
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO59_AO}    value=2.5
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO61_AO}    value=2.5
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO41_AO}    value=0.01

    DeviceUnderTest_CAN1.Set Minimum Logging Level To Critical
    # Reset all pin diagnostic
    BuiltIn.Run Keyword And Ignore Error
    ...    DeviceUnderTest_CAN1.Write Sdo   node_id=${APP_NODE_ID}   index_name=IO_Control  sub_name=Reset_Pin_Diagnostic  data=${True}
    BuiltIn.Sleep    0.1s
    BuiltIn.Run Keyword And Ignore Error
    ...    DeviceUnderTest_CAN1.Write Sdo   node_id=${APP_NODE_ID}   index_name=IO_Control  sub_name=Reset_Pin_Diagnostic  data=${False}
    DeviceUnderTest_CAN1.Set Minimum Logging Level To Default
