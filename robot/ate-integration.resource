*** Settings ***
Documentation       Main resource file for ATE test environment.

Resource            resources/libraries_and_variables.resource
Resource            resources/libraries_and_variables copy.resource
Resource            resources/power_management.resource
Resource            resources/can_management.resource
Resource            resources/artifact.resource
Resource            resources/dut.resource
Resource            resources/application_rpc_management.resource
Resource            resources/ate_io_variables.resource
Library             Dialogs


*** Keywords ***
Setup Bench
    [Documentation]    Keyword for Suite setup to make sure bench is set OK

    #XnetDbUtility.Register Xnet Databases

    #BuiltIn.Wait Until Keyword Succeeds    3 times    500ms
    #...    Veristand Stop, Start And Deploy  sdf_file=${VERISTAND_INTEGRATION_1_SDF_PATH}

    #AliasXmlParser.Compare Aliases Files
    #...    veristand_folder=${VERISTAND_PATH}
    #...    robot_resource_file_path=${VERISTAND_INTEGRATION_1_ALIASES_RESOURCE_PATH}

    DeviceUnderTest_CAN1.Connect    bustype=${CAN1_BUSTYPE}       channel=${CAN1_CHANNEL}          bitrate=${CAN1_BITRATE}

    DeviceUnderTest_CAN1.Add Node   node_id=${FW_NODE_ID}       eds_file_path=${FW_EDS_FILE}

    #VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_POWER_ENABLE_4}    value=1
    #Power On DUT

    Dialogs.Pause Execution    message=Power On DUT

    BuiltIn.Sleep    10s

    Verify DUT Hardware Revision And Device Name

    CodesysEthGateway.Execute
    ...    timeout=${CODESYS_GATEWAY_EXECUTION_START_TIMEOUT}

    BuiltIn.Wait Until Keyword Succeeds     3 times    500ms
    ...    CodesysRpcExecuter.Execute       timeout=${CODESYS_RPC_TIMEOUT_S}

    CodesysRpcClient.Connect
    Setup Application  ${CODESYS_TEST_PROJECT}

    Logout, Power Cycle And Login To Dut

    # Enable All ATE CAN Ports

Teardown Bench
    [Documentation]    Keyword for Suite setup to make sure bench is shut down OK

    Logout, Power Cycle And Login To Dut

    Add Firmware Metadata To Report
    Add Application Metadata To Report

    CodesysRpcClient.Logout
    CodesysRpcClient.Close Project
    CodesysRpcClient.Stop Remote Server
    BuiltIn.Sleep    10s
    CodesysEthGateway.Kill

    # Set 0V to BSL
    #VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_IO21_AO}    value=0

    #XnetDbUtility.Unregister Xnet Databases
    DeviceUnderTest_CAN1.Disconnect

    # Power Off DUT
    Dialogs.Pause Execution    message=Power off DUT
    #VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_POWER_ENABLE_4}    value=0

    #VeristandApi.Disconnect System And Undeploy Definition
    #VeristandApi.Stop    timeout_s=${VERISTAND_STOP_TIMEOUT_S}

Setup Application
    [Documentation]    Download new application
    [Arguments]    ${app_file}

    CodesysRpcClient.Set Default Credentials    username=${PLC_USERNAME}    password=${PASSWORD}
    CodesysRpcClient.Open Project    ${app_file}

    BuiltIn.Wait Until Keyword Succeeds     3 times    500ms
    ...    CodesysRpcClient.Set Communication Parameters
    ...    device_ip=localhost
    ...    device_name=${CODESYS_DEVICE_NAME}
    ...    gateway_name=Gateway-1

    IF    ${SAFETY_PRODUCT}    CodesysRpcClient.Enter Debug Mode

    CodesysRpcClient.Login

Setup Suite
    [Documentation]    Global suite setup.
    ...                - Logout and power-off DUT
    ...                - Check and deploy new SDF if needed
    ...                - Login with current application and check project name
    ...                - Download new application if needed
    [Arguments]    ${sdf_file}    ${app_file}

    #CodesysRpcClient.Logout
    # Power Off DUT

#    Setup VeriStand    ${sdf_file}

    # VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_POWER_ENABLE_4}    value=1
    # Power On DUT

    #BuiltIn.Sleep    5s

    BuiltIn.Wait Until Keyword Succeeds    2 times    100ms
    ...  CodesysRpcClient.Login Without Download

    # Check what application is running
    ${app_file_name} =  String.Fetch From Right  string=${app_file}    marker=\\
    ${app_file_name} =  String.Fetch From Left  string=${app_file_name}    marker=.
    ${app_info_project_name} =  Get Application Project Name
    ${app_info_project_name} =  String.Strip String  ${app_info_project_name}  characters=\'

    BuiltIn.Log  ${app_info_project_name}
    BuiltIn.Log  ${app_file_name}

    # Logout/Login and reboot with new application if needed
    IF  $app_info_project_name != $app_file_name
        # TODO BuiltIn.Run Keyword If    ${app_info_project_name} != '${app_file_name}'        This keyword was functional. Remove when IF is working.
        CodesysRpcClient.Logout
        Setup Application  ${app_file}
        Logout, Power Cycle And Login To Dut
    END

Teardown Suite
    [Documentation]    Todo
    Log  Todo

Setup Test
    [Documentation]    Keyword to setup test

    Logout, Power Cycle And Login To Dut

Teardown Test
    [Documentation]    Keyword to teardown test

    IF  $TEST_STATUS == 'FAIL'
        DeviceUnderTest_CAN1.Add Node    node_id=${FW_NODE_ID}
        ${error_logs} =    BuiltIn.Run Keyword And Warn On Failure
        ...    DeviceUnderTest_CAN1.Get Firmware Error Log Latest 25
        ...    fw_node_id=${FW_NODE_ID}
        BuiltIn.Log    ${error_logs}
    END

#    Check Veristand Alarms

#Setup VeriStand
#    [Documentation]    Check and deploy VeriStand system definition file.
#    [Arguments]        ${sdf_file}

    # Get deployment status
#    ${gw_status} =    VeristandApi.Get Deployment Status
#    Log               ${gw_status}

    # Check if deployed system definition matches keyword input argument
    # Check should fail also, if none system definition file is deployed
#    ${sdf_deployed} =  Set Variable    ${gw_status['systemdefinition_file']}
#    ${correct_sdf_deployed} =  Run Keyword And Return Status   Builtin.Should Be Equal As Strings
#    ...    first=${sdf_deployed}
#    ...    second=${sdf_file}
#    BuiltIn.Log  ${correct_sdf_deployed}

#    IF  not ${correct_sdf_deployed}
#        VeristandApi.Disconnect System And Undeploy Definition

#        BuiltIn.Wait Until Keyword Succeeds    3 times    500ms
#    ...    Veristand Stop, Start And Deploy  sdf_file=${sdf_file}
#    END

Logout, Power Cycle And Login To Dut
    [Documentation]  This must be as fast as possible.

    CodesysRpcClient.Logout

    # Power Cycle DUT
    Dialogs.Pause Execution    message=Power cycle DUT, press OK when DUT is operational

    BuiltIn.Wait Until Keyword Succeeds    2 times    100ms
    ...  CodesysRpcClient.Login Without Download

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

#Check Veristand Alarms
#    [Documentation]    Checks alarms from Veristand and stops execution if fault alarms are ON.

    #${status} =    BuiltIn.Run Keyword And Return Status    VeristandApi.Check Alarms

#    IF    not ${status}
#        BuiltIn.Fatal Error    msg=Alarms are ON, Test Execution needs to stop!
#    END

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

    ${content} =    Get Application Project Information
    OperatingSystem.Append To File
    ...    path=${PATH_TO_APP_METADATA}
    ...    content=Codesys project: ${content}[0]\n\n
    ...    encoding=UTF-8

    OperatingSystem.Append To File
    ...    path=${PATH_TO_APP_METADATA}
    ...    content=Application title: ${content}[1]\n\n
    ...    encoding=UTF-8

    OperatingSystem.Append To File
    ...    path=${PATH_TO_APP_METADATA}
    ...    content=Application version: ${content}[2]\n\n
    ...    encoding=UTF-8

    OperatingSystem.Append To File
    ...    path=${PATH_TO_APP_METADATA}
    ...    content=Device name: ${content}[3]\n\n
    ...    encoding=UTF-8

    OperatingSystem.Append To File
    ...    path=${PATH_TO_APP_METADATA}
    ...    content=Device version: ${content}[4]\n\n
    ...    encoding=UTF-8

#Veristand Stop, Start And Deploy
#    [Documentation]    Keyword to make sure NI Veristand is up and running and deployed.
#    [Arguments]        ${sdf_file}

#    VeristandApi.Stop       timeout_s=${VERISTAND_STOP_TIMEOUT_S}
#    VeristandApi.Start      timeout_s=${VERISTAND_START_TIMEOUT_S}
#    VeristandApi.Connect To System And Deploy Definition
#    ...    sdf_path=${sdf_file}
#    ...    deploy=${True}
#    ...    timeout_s=${VERISTAND_SDF_DEPLOY_TIMEOUT_S}

Convert PWM Timeout Seconds To FPGA Ticks
    [Documentation]       Calculates FPGA Ticks based user settable timeout value (s)
    ...
    ...                   Each second corresponds to 40M ticks (FPGA Reference clock is 40 MHz).
    [Arguments]    ${timeout_s}

    ${ticks} =    BuiltIn.Evaluate    ${timeout_s} * 40000000
    RETURN        ${ticks}
