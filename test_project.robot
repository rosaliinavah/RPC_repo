*** Settings ***
Documentation       Test Suite to verify codesys interface.

Resource            resources/libraries_and_variables copy.resource
Resource            resources/power_management.resource
Library             Dialogs

Suite Setup         Setup Bench Local
Suite Teardown      Teardown Bench Local
Test Setup          Setup Test Local
Test Teardown       Teardown Test Local


*** Variables ***
# PLC PRG Name
${PLC_PRG_NAME} =                   Test
${GPS_PRG_NAME} =                   GPS

# PLC variables
${PLC_UPDATE_VALUES_VARIABLE} =     ${PLC_PRG_NAME}.UpdateValues
${PLC_LATITUDE} =                   ${GPS_PRG_NAME}.GPS_Latitude
${PLC_LONGITUDE} =                  ${GPS_PRG_NAME}.GPS_Longitude
${PLC_ALTITUDE} =                   ${GPS_PRG_NAME}.GPS_Altitude
${PLC_PT100} =                      ${PLC_PRG_NAME}.PT100
${PLC_PT1000} =                     ${PLC_PRG_NAME}.PT1000

# Directories
${VUE_UI_DIR} =                     C:\\Codesys RPC\\UI
${BACKEND_DIR} =                    C:\\Codesys RPC


*** Test Cases ***
Test NodeJs Webserver
    [Documentation]    Testing

    Kill All Node Processes
    Start Backend Server
    Start Vue UI Server

    Log    Environment started successfully.

    VAR  ${update_values}   ${TRUE}

    # Stop sequence if enable button on the display is set to false
    WHILE    $update_values == 'TRUE'

        # Read variables from PLC using RPC
        ${PT100} =    CodesysRpcClient.Read Variable    ${PLC_PT100}
        ${PT1000} =   CodesysRpcClient.Read Variable    ${PLC_PT1000}
        ${LAT} =      CodesysRpcClient.Read Variable    ${PLC_LATITUDE}
        ${LON} =      CodesysRpcClient.Read Variable    ${PLC_LONGITUDE}
        ${ALT} =      CodesysRpcClient.Read Variable    ${PLC_ALTITUDE}

        # Set variables to JSON format
        VAR  ${json} =    {"pt100": ${PT100},"pt1000": ${PT1000},"latitude": ${LAT},"longitude": ${LON},"altitude": ${ALT}}

        # Create data.json file for server.js
        Create File    data.tmp    ${json}
        Move File      data.tmp    data.json

        # Check enable button state
        ${update_values} =    CodesysRpcClient.Read Variable    ${PLC_UPDATE_VALUES_VARIABLE}

        Log   message=${update_values}

        Sleep    1s
    END

    # Terminate processes and kill tasks
    Terminate Process    NodeServer
    Terminate Process    VueUI
    Sleep    2s
    Kill All Node Processes


*** Keywords ***
Setup Bench Local
    [Documentation]    Keyword for Suite setup to make sure Codesys and application are running.

    codesys_control_service_executer.Execute
    ...    timeout=${CODESYS_CONTROL_WIN_SERVICE_START_TIMEOUT}
    BuiltIn.Wait Until Keyword Succeeds    3 times    500ms
    ...    CodesysRpcExecuter.Execute    timeout=${CODESYS_START_TIMEOUT}
    CodesysRpcClient.Connect
    CodesysRpcClient.Set Default Credentials    username=${PLC_USERNAME}    password=${PASSWORD}
    CodesysRpcClient.Open Project    ${CODESYS_TEST_PROJECT}

    @{gateways} =  CodesysRpcClient.Find Gateway   name=Gateway-1
    ${nbr_of_gateways} =  BuiltIn.Get Length  item=${gateways}

    IF  ${nbr_of_gateways} == 0
        CodesysRpcClient.Add New Gateway   name=Gateway-1
    END

    CodesysRpcClient.Set Communication Parameters
    ...    device_ip=localhost
    ...    device_name=${PLC_DEVICE_NAME}
    ...    gateway_name=Gateway-1

    IF    ${SAFETY_PRODUCT}    CodesysRpcClient.Enter Debug Mode
    CodesysRpcClient.Login

    CodesysRpcClient.Reset Cold
    CodesysRpcClient.Start App

Teardown Bench Local
    [Documentation]    Keyword for Suite setup to make sure application and Codesys stopped.

    CodesysRpcClient.Logout
    CodesysRpcClient.Close Project
    CodesysRpcClient.Stop Remote Server
    codesys_control_service_executer.Kill

    Kill All Node Processes
    Terminate All Processes    kill=${TRUE}

Setup Test Local
    [Documentation]    Reset and start application

    CodesysRpcClient.Reset Warm
    CodesysRpcClient.Start App

Teardown Test Local
    [Documentation]    Keyword to teardown test

    #Log   message=Nothing to see here, yet

    # Terminate processes and kill tasks
    Terminate Process    NodeServer
    Terminate Process    VueUI
    Sleep    2s
    Kill All Node Processes

Kill All Node Processes
    [Documentation]    Kill old Node.js servers before starting a new one

    Log    Killing old Node processes...
    Run Process    taskkill    /F    /IM    node.exe    shell=True
    Sleep    2s

Start Vue UI Server
    [Documentation]    Start Vue.js UI in the background

    Log    Starting Vue UI...

    Start Process
    ...    cmd
    ...    /c npm run dev
    ...    cwd=${VUE_UI_DIR}
    ...    stdout=vue_out.txt
    ...    stderr=vue_err.txt
    ...    alias=VueUI
    Sleep    8s

Start Backend Server
    [Documentation]    Start server.js in the background

    Log    Starting Node backend...

    Start Process
    ...    cmd
    ...    /c node server.js
    ...    cwd=${BACKEND_DIR}
    ...    stdout=server_out.txt
    ...    stderr=server_err.txt
    ...    alias=NodeServer
    Sleep    5s
