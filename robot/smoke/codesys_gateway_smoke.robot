*** Settings ***
Documentation       Smoke test to verify Codesys Gateway functionalities to mitigate risks it start to fail due driver update etc.

Resource            resources/libraries_and_variables copy.resource
Resource            resources/power_management.resource
#Resource            resources/automatic_test_environment.resource

Suite Setup         Setup Bench Local
Suite Teardown      Teardown Bench Local
Test Setup          Setup Test Local
Test Teardown       Teardown Test Local


*** Test Cases ***
Verify Codesys Can Gateway Start
    [Documentation]    Verifies that CAN Gateway is able to start on Windows.
    [Tags]    smoke    virtual

    BuiltIn.Log   Start codesys gateway: ${CODESYS_CAN_GATEWAY_LOCATION}
    CodesysCanGateway.Execute

    ${gateway_process_id} =  CodesysCanGateway.Get Pid
    BuiltIn.Log   Gateway process id: ${gateway_process_id}

    BuiltIn.Log   Process should be running.
    BuiltIn.Should Be True   ${gateway_process_id} != ${0}

Verify Codesys Can Gateway Stop
    [Documentation]    Verifies that CAN Gateway is able to stop on Windows.
    [Tags]    smoke    virtual

    BuiltIn.Log   Stop codesys gateway: ${CODESYS_CAN_GATEWAY_LOCATION}
    CodesysCanGateway.Kill

    ${gateway_process_id} =  CodesysCanGateway.Get Pid
    BuiltIn.Log   Gateway process id: ${gateway_process_id}

    BuiltIn.Log   Process should be closed.
    Builtin.Should Be Equal As Numbers    first=${gateway_process_id}    second=${0}

Verify Codesys Eth Gateway Start
    [Documentation]    Verifies that ETH Gateway is able to start on Windows.
    [Tags]    smoke    virtual

    BuiltIn.Log   Start codesys gateway: ${CODESYS_ETH_GATEWAY_LOCATION}
    CodesysEthGateway.Execute

    ${gateway_process_id} =  CodesysEthGateway.Get Pid
    BuiltIn.Log   Gateway process id: ${gateway_process_id}

    BuiltIn.Log   Process should be running.
    BuiltIn.Should Be True   ${gateway_process_id} != ${0}

Verify Codesys Eth Gateway Stop
    [Documentation]    Verifies that ETH Gateway is able to stop on Windows.
    [Tags]    smoke    virtual

    BuiltIn.Log   Stop codesys gateway: ${CODESYS_ETH_GATEWAY_LOCATION}
    CodesysEthGateway.Kill

    ${gateway_process_id} =  CodesysEthGateway.Get Pid
    BuiltIn.Log   Gateway process id: ${gateway_process_id}

    BuiltIn.Log   Process should be closed.
    Builtin.Should Be Equal As Numbers    first=${gateway_process_id}    second=${0}


*** Keywords ***
Setup Bench Local
    [Documentation]    Keyword for Suite setup to make sure bench is set OK

    BuiltIn.Log    Keyword for Suite setup to make sure bench is set OK

Teardown Bench Local
    [Documentation]    Local Suite Teardown

    Teardown Bench

    BuiltIn.Log   Stop codesys gateways
    CodesysCanGateway.Kill
    CodesysEthGateway.Kill

Setup Test Local
    [Documentation]    Keyword to setup test

    BuiltIn.Log    Keyword to setup test

Teardown Test Local
    [Documentation]    Keyword to teardown test

    BuiltIn.Log    Keyword to teardown test