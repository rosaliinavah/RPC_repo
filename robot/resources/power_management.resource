*** Settings ***
Documentation       Resource file for Power Management such as power cycle DUT.

Resource            libraries_and_variables.resource


*** Keywords ***
Power On DUT
    [Documentation]    Power on DUT using Veristand API with Aliases

    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_POWER_ENABLE_RMX}    value=1

Power Off DUT
    [Documentation]    Power off DUT using Veristand API with Aliases

    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_POWER_ENABLE_RMX}    value=0

Power Cycle DUT
    [Documentation]    Power cycle DUT using existing keywords with Veristand API and Aliases

    Power Off DUT
    BuiltIn.Sleep    5s    reason=Wait for HW to completely power-off

    Power On DUT
    BuiltIn.Sleep    5s    reason=Wait for application to bootup

Power Cycle DUT And Wait For Bootup Message
    [Documentation]    Power cycle DUT using existing keywords with Veristand API and Aliases
    [Arguments]        ${node_id}    ${timeout}=5

    Power Off DUT
    BuiltIn.Sleep    5s    reason=Wait for HW to completely power-off

    Power On DUT
    DeviceUnderTest_CAN1.Wait Boot Up Message    ${node_id}      timeout=${timeout}

    BuiltIn.Sleep    100ms   reason=Bootup message is sent before Safety Test is ran in application code
