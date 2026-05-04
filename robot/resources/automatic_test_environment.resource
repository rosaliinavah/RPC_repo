*** Settings ***
Documentation       Main resource file for ATE test environment.

Resource            resources/libraries_and_variables.resource
Resource            resources/power_management.resource


*** Keywords ***
Setup Bench
    [Documentation]    Keyword for Suite setup to make sure bench is set OK

    BuiltIn.Log    Keyword for Suite setup to make sure bench is set OK

Teardown Bench
    [Documentation]    Keyword for Suite setup to make sure bench is shut down OK

    BuiltIn.Log    Keyword for Suite setup to make sure bench is shut down OK

Setup Test
    [Documentation]    Keyword to setup test

    BuiltIn.Log    Keyword to setup test

Teardown Test
    [Documentation]    Keyword to teardown test

    BuiltIn.Log    Keyword to teardown test
