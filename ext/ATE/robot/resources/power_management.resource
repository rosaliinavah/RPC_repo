*** Settings ***
Documentation       Resource file for power management of ATE.

Resource            libraries_and_variables.resource


*** Keywords ***
Power On DUT
    [Documentation]    Power on DUT

    BuiltIn.Log    veristand_api.Write Channel Value channel_name=${ALIASES_ATE_IO10_AO} value=1

Power Off DUT
    [Documentation]    Power off DUT

    BuiltIn.Log    veristand_api.Write Channel Value channel_name=${ALIASES_ATE_IO10_AO} value=0

Power Cycle DUT
    [Documentation]    Power cycle DUT

    BuiltIn.Log    veristand_api.Write Channel Value channel_name=${ALIASES_ATE_IO10_AO} value=0
    BuiltIn.Sleep    2s
    BuiltIn.Log    veristand_api.Write Channel Value channel_name=${ALIASES_ATE_IO10_AO} value=1
    BuiltIn.Sleep    2s
