*** Settings ***
Documentation       Test Suite to verify codesys interface.

Resource            automatic_test_environment.resource

Suite Setup         Setup Bench Local
Suite Teardown      Teardown Bench Local
Test Setup          Setup Test Local
Test Teardown       Teardown Test Local


*** Variables ***
# PLC PRG Name
${PLC_PRG_NAME} =                   PLC_PRG

# Basic PLC variables
${PLC_INT_VARIABLE} =               ${PLC_PRG_NAME}.intVariable
${PLC_REAL_VARIABLE} =              ${PLC_PRG_NAME}.realVariable
${PLC_BOOL_VARIABLE} =              ${PLC_PRG_NAME}.boolVariable
${PLC_STRING_VARIABLE} =            ${PLC_PRG_NAME}.stringVariable
${PLC_DINT_VARIABLE} =              ${PLC_PRG_NAME}.dintVariable
${PLC_BYTE_VARIABLE} =              ${PLC_PRG_NAME}.byteVariable

# Struct variable
${PLC_STRUCT_VARIABLE_INT} =        ${PLC_PRG_NAME}.structVariable.intVariable
${PLC_STRUCT_VARIABLE_REAL} =       ${PLC_PRG_NAME}.structVariable.realVariable

# PLC Timer variable
${PLC_TIMER_ENABLE} =               ${PLC_PRG_NAME}.timerVariable.IN
${PLC_TIMER_SAFETIME} =             ${PLC_PRG_NAME}.timerVariable.PT
${PLC_TIMER_REACHED_END} =          ${PLC_PRG_NAME}.timerVariable.Q
${PLC_TIMER_ELAPSED_TIME} =         ${PLC_PRG_NAME}.timerVariable.ET

# PLC Counter variable
${PLC_COUNTER_INCREMENT} =          ${PLC_PRG_NAME}.counterVariable.CU
${PLC_COUNTER_RESET} =              ${PLC_PRG_NAME}.counterVariable.RESET
${PLC_COUNTER_UPPER_LIMIT} =        ${PLC_PRG_NAME}.counterVariable.PV
${PLC_COUNTER_LIMIT_REACHED} =      ${PLC_PRG_NAME}.counterVariable.Q
${PLC_COUNTER_COUNTER_VALUE} =      ${PLC_PRG_NAME}.counterVariable.CV

${PLC_INT_ARRAY} =                  ${PLC_PRG_NAME}.intArray

# PLC BOOLEANS
${TRUE} =                           TRUE
${FALSE} =                          FALSE


*** Test Cases ***
Test PLC Logic with Integer and Real Variables
    [Documentation]    Testing PLC logic using Integer and Real variables.
    [Tags]    smoke    virtual

    ${int_value} =    codesys_rpc_client.Read Variable    ${PLC_INT_VARIABLE}
    ${real_value} =    codesys_rpc_client.Read Variable    ${PLC_REAL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${int_value}    second=0
    Builtin.Should Be Equal As Strings    first=${real_value}    second=0

    ${int_value} =    BuiltIn.Convert To Integer    26
    codesys_rpc_client.Write Variable    ${PLC_INT_VARIABLE}    value=${int_value}
    ${real_value} =    codesys_rpc_client.Read Variable    ${PLC_REAL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${real_value}    second=25

    codesys_rpc_client.Write Variable    ${PLC_INT_VARIABLE}    value=51
    ${real_value} =    codesys_rpc_client.Read Variable    ${PLC_REAL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${real_value}    second=50

    codesys_rpc_client.Write Variable    ${PLC_INT_VARIABLE}    value=76
    ${real_value} =    codesys_rpc_client.Read Variable    ${PLC_REAL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${real_value}    second=75

    codesys_rpc_client.Write Variable    ${PLC_INT_VARIABLE}    value=101
    ${real_value} =    codesys_rpc_client.Read Variable    ${PLC_REAL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${real_value}    second=100

    ${values_dict} =    codesys_rpc_client.Read Variables
    ...    ${PLC_INT_VARIABLE}
    ...    ${PLC_REAL_VARIABLE}
    ...    ret_type=bin
    Builtin.Should Be Equal As Strings    first=${values_dict}[${PLC_INT_VARIABLE}]    second=0b1100101
    Builtin.Should Be Equal As Strings    first=${values_dict}[${PLC_REAL_VARIABLE}]    second=0b1100100

Test PLC Logic with Boolean Variable
    [Documentation]    Testing PLC logic using Boolean variables.
    [Tags]    smoke    virtual

    ${bool_value} =    codesys_rpc_client.Read Variable    ${PLC_BOOL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${bool_value}    second=${FALSE}
    codesys_rpc_client.Write Variable    ${PLC_BOOL_VARIABLE}    value=${TRUE}
    ${bool_value} =    codesys_rpc_client.Read Variable    ${PLC_BOOL_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${bool_value}    second=${TRUE}

Test PLC Logic with String Variable
    [Documentation]    Testing PLC logic using String variables.
    [Tags]    smoke    virtual

    ${string_value} =    codesys_rpc_client.Read Variable    ${PLC_STRING_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${string_value}    second='Wirva Solutions Oy!'
    codesys_rpc_client.Write Variable    ${PLC_STRING_VARIABLE}    value='Amazing'
    ${string_value} =    codesys_rpc_client.Read Variable    ${PLC_STRING_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${string_value}    second='Amazing'

Test PLC Logic with DInteger Variable
    [Documentation]    Testing PLC logic using DInteger variables.
    [Tags]    smoke    virtual

    ${dint_value} =    codesys_rpc_client.Read Variable    ${PLC_DINT_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${dint_value}    second=0
    codesys_rpc_client.Write Variable    ${PLC_DINT_VARIABLE}    value=123456
    ${dint_value} =    codesys_rpc_client.Read Variable    ${PLC_DINT_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${dint_value}    second=123456

    codesys_rpc_client.Write Variables    ${PLC_INT_VARIABLE}=123    ${PLC_DINT_VARIABLE}=0b1110 1010
    ${values_dict} =    codesys_rpc_client.Read Variables
    ...    ${PLC_INT_VARIABLE}
    ...    ${PLC_DINT_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${values_dict}[${PLC_INT_VARIABLE}]    second=123
    Builtin.Should Be Equal As Strings    first=${values_dict}[${PLC_DINT_VARIABLE}]    second=234

Test PLC Logic with Byte Variable
    [Documentation]    Testing PLC logic using Byte variables.
    [Tags]    smoke    virtual

    ${byte_value} =    codesys_rpc_client.Read Variable    ${PLC_BYTE_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=0
    codesys_rpc_client.Write Variable    ${PLC_BYTE_VARIABLE}    value=55
    ${byte_value} =    codesys_rpc_client.Read Variable    ${PLC_BYTE_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=55

    codesys_rpc_client.Write Variable    ${PLC_BYTE_VARIABLE}    value=0xF0
    ${byte_value} =    codesys_rpc_client.Read Variable    ${PLC_BYTE_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=240

    codesys_rpc_client.Write Variable    ${PLC_BYTE_VARIABLE}    value=0b11111000
    ${byte_value} =    codesys_rpc_client.Read Variable    ${PLC_BYTE_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=248

    codesys_rpc_client.Write Variable    ${PLC_BYTE_VARIABLE}    value=2#11111001
    ${byte_value} =    codesys_rpc_client.Read Variable    ${PLC_BYTE_VARIABLE}
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=249

    codesys_rpc_client.Write Variable    ${PLC_BYTE_VARIABLE}    value=16#FF
    ${byte_value} =    codesys_rpc_client.Read Variable    ${PLC_BYTE_VARIABLE}    ret_type=bin
    Builtin.Should Be Equal As Strings    first=${byte_value}    second=0b11111111

Test PLC Logic with Integer Array Variable
    [Documentation]    Testing PLC logic using DInteger variables.
    [Tags]    smoke    virtual

    ${array_index_zero} =    BuiltIn.Catenate    ${PLC_INT_ARRAY}    [0]
    ${array_value} =    codesys_rpc_client.Read Variable    ${array_index_zero}
    Builtin.Should Be Equal As Strings    first=${array_value}    second=0

    ${array_index_zero} =    BuiltIn.Catenate    ${PLC_INT_ARRAY}    [3]
    ${array_value} =    codesys_rpc_client.Read Variable    ${array_index_zero}
    Builtin.Should Be Equal As Strings    first=${array_value}    second=3

Test PLC Logic with Struct Variable
    [Documentation]    Testing PLC logic using Struct variables.
    [Tags]    smoke    virtual

    ${int_value} =    codesys_rpc_client.Read Variable    ${PLC_STRUCT_VARIABLE_INT}
    ${real_value} =    codesys_rpc_client.Read Variable    ${PLC_STRUCT_VARIABLE_REAL}
    Builtin.Should Be Equal As Strings    first=${int_value}    second=0
    Builtin.Should Be Equal As Strings    first=${real_value}    second=0

    codesys_rpc_client.Write Variable    ${PLC_STRUCT_VARIABLE_INT}    value=255
    ${int_value} =    codesys_rpc_client.Read Variable    ${PLC_STRUCT_VARIABLE_INT}
    Builtin.Should Be Equal As Strings    first=${int_value}    second=255

    codesys_rpc_client.Write Variable    ${PLC_STRUCT_VARIABLE_REAL}    value=255
    ${real_value} =    codesys_rpc_client.Read Variable    ${PLC_STRUCT_VARIABLE_REAL}
    Builtin.Should Be Equal As Strings    first=${real_value}    second=255

Test PLC Logic with Timer Function Block
    [Documentation]    Testing PLC logic using Timer Function Block.
    ...    Timer limit is set to 5s in PLC code.
    [Tags]    smoke    virtual

    codesys_rpc_client.Write Variable    ${PLC_TIMER_SAFETIME}    value=T#5S
    codesys_rpc_client.Write Variable    ${PLC_TIMER_ENABLE}    value=${TRUE}
    ${bool_value} =    codesys_rpc_client.Read Variable    ${PLC_TIMER_REACHED_END}
    BuiltIn.Should Be Equal As Strings    first=${bool_value}    second=${FALSE}

    BuiltIn.Sleep    3s

    ${bool_value} =    codesys_rpc_client.Read Variable    ${PLC_TIMER_REACHED_END}
    BuiltIn.Should Be Equal As Strings    first=${bool_value}    second=${FALSE}

    BuiltIn.Sleep    3s

    ${bool_value} =    codesys_rpc_client.Read Variable    ${PLC_TIMER_REACHED_END}
    BuiltIn.Should Be Equal As Strings    first=${bool_value}    second=${TRUE}

    ${time_value} =    codesys_rpc_client.Read Variable    ${PLC_TIMER_ELAPSED_TIME}
    BuiltIn.Should Be Equal As Strings    first=${time_value}    second=5s

Test PLC Logic with Counter Function Block
    [Documentation]    Testing PLC logic using Counter Function Block.
    ...    Counter is used to count rising edges to ${PLC_PRG_NAME}.counterVariable.CU.
    [Tags]    smoke    virtual

    codesys_rpc_client.Write Variable    variable=${PLC_COUNTER_UPPER_LIMIT}    value=10

    FOR    ${index}    IN RANGE    15
        codesys_rpc_client.Write Variable    variable=${PLC_COUNTER_INCREMENT}    value=${TRUE}
        codesys_rpc_client.Write Variable    variable=${PLC_COUNTER_INCREMENT}    value=${FALSE}
    END

    ${int_value} =    codesys_rpc_client.Read Variable    ${PLC_COUNTER_COUNTER_VALUE}
    Builtin.Should Be Equal As Strings    first=${int_value}    second=15

    ${bool_value} =    codesys_rpc_client.Read Variable    ${PLC_COUNTER_LIMIT_REACHED}
    Builtin.Should Be Equal As Strings    first=${bool_value}    second=${TRUE}


*** Keywords ***
Setup Bench Local
    [Documentation]    Keyword for Suite setup to make sure Codesys and application are running.

    codesys_control_service_executer.Execute
    ...    timeout=${CODESYS_CONTROL_WIN_SERVICE_START_TIMEOUT}
    BuiltIn.Wait Until Keyword Succeeds    3 times    500ms
    ...    codesys_rpc_executer.Execute    timeout=${CODESYS_START_TIMEOUT}
    codesys_rpc_client.Connect
    codesys_rpc_client.Set Default Credentials    username=${PLC_USERNAME}    password=${PLC_PASSWORD}
    codesys_rpc_client.Open Project    ${CODESYS_TEST_APP_PROJECT}

    @{gateways} =  codesys_rpc_client.Find Gateway   name=Gateway-1
    ${nbr_of_gateways} =  BuiltIn.Get Length  item=${gateways}

    IF  ${nbr_of_gateways} == 0
        codesys_rpc_client.Add New Gateway   name=Gateway-1
    END

    codesys_rpc_client.Set Communication Parameters
    ...    device_ip=localhost
    ...    device_name=${PLC_DEVICE_NAME}
    ...    gateway_name=Gateway-1

    IF    ${SAFETY_PRODUCT}    codesys_rpc_client.Enter Debug Mode
    codesys_rpc_client.Login

Teardown Bench Local
    [Documentation]    Keyword for Suite setup to make sure application and Codesys stopped.

    codesys_rpc_client.Logout
    codesys_rpc_client.Close Project
    codesys_rpc_client.Stop Remote Server
    codesys_control_service_executer.Kill

Setup Test Local
    [Documentation]    Reset and start application

    codesys_rpc_client.Reset Warm
    codesys_rpc_client.Start App

Teardown Test Local
    [Documentation]    Keyword to teardown test

    Log    Nothing to see here, yet
