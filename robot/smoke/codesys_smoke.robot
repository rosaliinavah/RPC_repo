*** Settings ***
Documentation       Test Suite to verify codesys interface.
...
...                 To be able to run this Suite PC needs:
...                 - Codesys
...                 - Codesys Control Win V3 automatically started from Windows Services

Resource            resources/libraries_and_variables copy.resource
Resource            resources/power_management.resource
#Resource            resources/automatic_test_environment.resource

Suite Setup         Setup Bench Local
Suite Teardown      Teardown Bench Local
Test Setup          Setup Test Local
Test Teardown       Teardown Test Local


*** Variables ***
# Basic PLC variables
${PLC_INT_VARIABLE} =               PLC_PRG.intVariable
${PLC_REAL_VARIABLE} =              PLC_PRG.realVariable
${PLC_BOOL_VARIABLE} =              PLC_PRG.boolVariable
${PLC_STRING_VARIABLE} =            PLC_PRG.stringVariable
${PLC_DINT_VARIABLE} =              PLC_PRG.dintVariable
${PLC_BYTE_VARIABLE} =              PLC_PRG.byteVariable

# Struct variable
${PLC_STRUCT_VARIABLE_INT} =        PLC_PRG.structVariable.intVariable
${PLC_STRUCT_VARIABLE_REAL} =       PLC_PRG.structVariable.realVariable

# PLC Timer variable
${PLC_TIMER_ENABLE} =               PLC_PRG.timerVariable.IN
${PLC_TIMER_SAFETIME} =             PLC_PRG.timerVariable.PT
${PLC_TIMER_REACHED_END} =          PLC_PRG.timerVariable.Q
${PLC_TIMER_ELAPSED_TIME} =         PLC_PRG.timerVariable.ET

# PLC Counter variable
${PLC_COUNTER_INCREMENT} =          PLC_PRG.counterVariable.CU
${PLC_COUNTER_RESET} =              PLC_PRG.counterVariable.RESET
${PLC_COUNTER_UPPER_LIMIT} =        PLC_PRG.counterVariable.PV
${PLC_COUNTER_LIMIT_REACHED} =      PLC_PRG.counterVariable.Q
${PLC_COUNTER_COUNTER_VALUE} =      PLC_PRG.counterVariable.CV

${PLC_INT_ARRAY} =                  PLC_PRG.intArray

# PLC BOOLEANS
${TRUE} =                           TRUE
${FALSE} =                          FALSE


*** Test Cases ***
Test PLC Logic with Integer and Real Variables
    [Documentation]    Testing PLC logic using Integer and Real variables.
    [Tags]    smoke    virtual

    ${int_value} =    codesys_client.Read Value    ${PLC_INT_VARIABLE}
    ${real_value} =    codesys_client.Read Value    ${PLC_REAL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${int_value}    second=0
    Builtin.Should Be Equal As Strings    first=${real_value}    second=0

    ${int_value} =    BuiltIn.Convert To Integer    26
    codesys_client.Write Value    ${PLC_INT_VARIABLE}    value=${int_value}
    ${real_value} =    codesys_client.Read Value    ${PLC_REAL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${real_value}    second=25

    codesys_client.Write Value    ${PLC_INT_VARIABLE}    value=51
    ${real_value} =    codesys_client.Read Value    ${PLC_REAL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${real_value}    second=50

    codesys_client.Write Value    ${PLC_INT_VARIABLE}    value=76
    ${real_value} =    codesys_client.Read Value    ${PLC_REAL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${real_value}    second=75

    codesys_client.Write Value    ${PLC_INT_VARIABLE}    value=101
    ${real_value} =    codesys_client.Read Value    ${PLC_REAL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${real_value}    second=100

Test PLC Logic with Boolean Variable
    [Documentation]    Testing PLC logic using Boolean variables.
    [Tags]    smoke    virtual

    ${bool_value} =    codesys_client.Read Value    ${PLC_BOOL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${bool_value}    second=${FALSE}
    codesys_client.Write Value    ${PLC_BOOL_VARIABLE}    value=${TRUE}
    ${bool_value} =    codesys_client.Read Value    ${PLC_BOOL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${bool_value}    second=${TRUE}

Test PLC Logic with String Variable
    [Documentation]    Testing PLC logic using String variables.
    [Tags]    smoke    virtual

    ${string_value} =    codesys_client.Read Value    ${PLC_STRING_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${string_value}    second='Wirva Solutions Oy!'
    codesys_client.Write Value    ${PLC_STRING_VARIABLE}    value='Amazing'
    ${string_value} =    codesys_client.Read Value    ${PLC_STRING_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${string_value}    second='Amazing'

Test PLC Logic with DInteger Variable
    [Documentation]    Testing PLC logic using DInteger variables.
    [Tags]    smoke    virtual

    ${dint_value} =    codesys_client.Read Value    ${PLC_DINT_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${dint_value}    second=0
    codesys_client.Write Value    ${PLC_DINT_VARIABLE}    value=123456
    ${dint_value} =    codesys_client.Read Value    ${PLC_DINT_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${dint_value}    second=123456

Test PLC Logic with Byte Variable
    [Documentation]    Testing PLC logic using Byte variables.
    [Tags]    smoke    virtual

    ${byte_value} =    codesys_client.Read Value    ${PLC_BYTE_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=0
    codesys_client.Write Value    ${PLC_BYTE_VARIABLE}    value=55
    ${byte_value} =    codesys_client.Read Value    ${PLC_BYTE_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=55

    codesys_client.Write Value    ${PLC_BYTE_VARIABLE}    value=0xF0
    ${byte_value} =    codesys_client.Read Value    ${PLC_BYTE_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=240

    codesys_client.Write Value    ${PLC_BYTE_VARIABLE}    value=0b11111000
    ${byte_value} =    codesys_client.Read Value    ${PLC_BYTE_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=248

    codesys_client.Write Value    ${PLC_BYTE_VARIABLE}    value=2#11111001
    ${byte_value} =    codesys_client.Read Value    ${PLC_BYTE_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=249

    codesys_client.Write Value    ${PLC_BYTE_VARIABLE}    value=16#FF
    ${byte_value} =    codesys_client.Read Value    ${PLC_BYTE_VARIABLE}    ret_type=bin
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=0b11111111

Test PLC Logic with Integer Array Variable
    [Documentation]    Testing PLC logic using DInteger variables.
    [Tags]    smoke    virtual

    ${array_index_zero} =    BuiltIn.Catenate    ${PLC_INT_ARRAY}    [0]
    ${array_value} =    codesys_client.Read Value    ${array_index_zero}
    Builtin.Should Be Equal As Strings    first=${array_value}    second=0

    ${array_index_zero} =    BuiltIn.Catenate    ${PLC_INT_ARRAY}    [3]
    ${array_value} =    codesys_client.Read Value    ${array_index_zero}
    Builtin.Should Be Equal As Strings    first=${array_value}    second=3

Test PLC Logic with Struct Variable
    [Documentation]    Testing PLC logic using Struct variables.
    [Tags]    smoke    virtual

    ${int_value} =    codesys_client.Read Value    ${PLC_STRUCT_VARIABLE_INT}
    ${real_value} =    codesys_client.Read Value    ${PLC_STRUCT_VARIABLE_REAL}
    Builtin.Should Be Equal As Strings    first=${int_value}    second=0
    Builtin.Should Be Equal As Strings    first=${real_value}    second=0

    codesys_client.Write Value    ${PLC_STRUCT_VARIABLE_INT}    value=255
    ${int_value} =    codesys_client.Read Value    ${PLC_STRUCT_VARIABLE_INT}
    Builtin.Should Be Equal As Strings    first=${int_value}    second=255

    codesys_client.Write Value    ${PLC_STRUCT_VARIABLE_REAL}    value=255
    ${real_value} =    codesys_client.Read Value    ${PLC_STRUCT_VARIABLE_REAL}
    Builtin.Should Be Equal As Strings    first=${real_value}    second=255

Test PLC Logic with Timer Function Block
    [Documentation]    Testing PLC logic using Timer Function Block.
    ...    Timer limit is set to 5s in PLC code.
    [Tags]    smoke    virtual

    codesys_client.Write Value    ${PLC_TIMER_SAFETIME}    value=T#5S
    codesys_client.Write Value    ${PLC_TIMER_ENABLE}    value=${TRUE}
    ${bool_value} =    codesys_client.Read Value    ${PLC_TIMER_REACHED_END}
    BuiltIn.Should Be Equal As Strings    first=${bool_value}    second=${FALSE}

    BuiltIn.Sleep    2s

    ${bool_value} =    codesys_client.Read Value    ${PLC_TIMER_REACHED_END}
    BuiltIn.Should Be Equal As Strings    first=${bool_value}    second=${FALSE}

    BuiltIn.Sleep    3s

    ${bool_value} =    codesys_client.Read Value    ${PLC_TIMER_REACHED_END}
    BuiltIn.Should Be Equal As Strings    first=${bool_value}    second=${TRUE}

    ${time_value} =    codesys_client.Read Value    ${PLC_TIMER_ELAPSED_TIME}
    BuiltIn.Should Be Equal As Strings    first=${time_value}    second=5s

Test PLC Logic with Counter Function Block
    [Documentation]    Testing PLC logic using Counter Function Block.
    ...    Counter is used to count rising edges to PLC_PRG.counterVariable.CU.
    [Tags]    smoke    virtual

    codesys_client.Write Value    param=${PLC_COUNTER_UPPER_LIMIT}    value=10

    FOR    ${index}    IN RANGE    15
        codesys_client.Write Value    param=${PLC_COUNTER_INCREMENT}    value=${TRUE}
        codesys_client.Write Value    param=${PLC_COUNTER_INCREMENT}    value=${FALSE}
    END

    ${int_value} =    codesys_client.Read Value    ${PLC_COUNTER_COUNTER_VALUE}
    Builtin.Should Be Equal As Strings    first=${int_value}    second=15

    ${bool_value} =    codesys_client.Read Value    ${PLC_COUNTER_LIMIT_REACHED}
    Builtin.Should Be Equal As Strings    first=${bool_value}    second=${TRUE}


*** Keywords ***
Setup Bench Local
    [Documentation]    Keyword for Suite setup to make sure Codesys and application are running.

    codesys_control_service_executer.Execute    timeout=${CODESYS_CONTROL_WIN_SERVICE_START_TIMEOUT}
    ${tmp} =   codesys_control_service_executer.Get Pid
    BuiltIn.Wait Until Keyword Succeeds    3 times    500ms
    ...    codesys_executer.Exec Codesys    script=${CODESYS_SERVER_API}    timeout=${CODESYS_START_TIMEOUT}

    codesys_client.Open Project    ${CODESYS_TEST_APP_PROJECT}

    @{gateways} =  codesys_client.Get Gateways
    ${nbr_of_gateways} =  BuiltIn.Get Length  item=${gateways}

    IF  ${nbr_of_gateways} == 0
        codesys_client.Set Gateway   gateway=Gateway-1
    END

    codesys_client.Set Default Credentials    username=${PLC_USERNAME}    password=${PLC_PASSWORD}

    codesys_client.Update Device    device=Device    version=${CODESYS_DEVICE_VERSION}
    codesys_client.Set Gateway    gateway=Gateway-1

    ${device_address} =    codesys_client.Scan Network
    Builtin.Log    Devices in network: ${device_address}

    #codesys_client.Set Address From Ip  ip=${device_address}  # ip=${PLC_DEVICE_IP}
    codesys_client.Set Address From Ip  ip=${PLC_DEVICE_IP}

    codesys_client.Conf Device Gateway And Address
    codesys_client.Login To Onlineapp
    codesys_client.Start App

Teardown Bench Local
    [Documentation]    Keyword for Suite setup to make sure application and Codesys stopped.

    codesys_client.Stop App
    codesys_client.Logout From Onlineapp
    codesys_client.Close Project
    codesys_client.Shutdown Server
    codesys_control_service_executer.Kill

Setup Test Local
    [Documentation]    Reset and start application

    codesys_client.Warm Reset
    codesys_client.Start App

Teardown Test Local
    [Documentation]    Keyword to teardown test

    Builtin.Log    Nothing to see here, yet
