*** Settings ***
Documentation       Test Suite for demostration.

Resource            ../automatic_test_environment.resource

Suite Setup         Setup Bench
Suite Teardown      Teardown Bench
Test Setup          Setup Test
Test Teardown       Teardown Test


*** Variables ***
# Basic PLC variables
${DEMO_VARIABLE} =      demo_value


*** Test Cases ***
Test Case for Demonstration Purposes First
    [Documentation]    Demo test case.
    [Tags]    release    smoke

    BuiltIn.Log    Demo test case ran.

Test Case for Demonstration Purposes Second
    [Documentation]    Demo test case.
    [Tags]    release

    BuiltIn.Log    Demo test case ran.
