*** Settings ***
Documentation       Smoke test to verify library interfaces are working after code changes.
...
...                 Aliases in Veristand Demo Engine project:
...
...                 Targets/Controller/Simulation Models/Models/Engine Demo/Outports/EngineTemp    EngineTemp
...                 Targets/Controller/Simulation Models/Models/Engine Demo/Outports/RPM    ActualRPM
...                 Targets/Controller/Simulation Models/Models/Engine Demo/Inports/command_EngineOn    EnginePower
...                 Targets/Controller/Simulation Models/Models/Engine Demo/Inports/command_RPM    DesiredRPM
...                 Targets/Controller/Calculated Channels/RPM Acceleration    Engine Calculations/RPM Acceleration
...                 Targets/Controller/User Channels/Calculations/RPM Velocity    Engine Calculations/RPM Velocity
...                 Targets/Controller/Calculated Channels/Engine Revolutions    Engine Calculations/Engine Revolutions
...                 Targets/Controller/User Channels/Calculations/RPM Offset    Engine Calculations/RPM Offset
...                 Targets/Controller/User Channels/Calculations/RPM Valley    Engine Calculations/RPM Valley
...                 Targets/Controller/Calculated Channels/RPM Peak    Engine Calculations/RPM Peak
...                 Targets/Controller/Calculated Channels/RPM Set Point Difference    Engine Calculations/RPM Set Point Difference
...                 Targets/Controller/User Channels/Safety Limits/Engine Temperature Alert    Engine Safety Limits/Engine Temperature Alert
...                 Targets/Controller/User Channels/Safety Limits/Engine Temperature Warning    Engine Safety Limits/Engine Temperature Warning

Resource            automatic_test_environment.resource

Suite Setup         Setup Bench Local
Suite Teardown      Teardown Bench Local
Test Setup          Setup Test Local
Test Teardown       Teardown Test Local


*** Test Cases ***
Verify Veristand API using Engine Demo Project
    [Documentation]    Verifies veristand python API using Engine Demo project which is running on Windows.
    [Tags]    smoke    ate

    ${act_rpm} =    veristand_api.Read Channel Value    channel_name=ActualRPM
    ${des_rpm} =    veristand_api.Read Channel Value    channel_name=DesiredRPM
    Builtin.Should Be Equal As Numbers    first=${act_rpm}    second=${0.0}
    Builtin.Should Be Equal As Numbers    first=${des_rpm}    second=${0.0}

    ${rpm_acc} =    veristand_api.Read Channel Value    channel_name=Engine Calculations/RPM Acceleration
    Builtin.Should Be Equal As Numbers    first=${rpm_acc}    second=${0.0}

    veristand_api.Write Channel Value    channel_name=DesiredRPM    value=0
    veristand_api.Write Channel Value    channel_name=EnginePower    value=1
    BuiltIn.Sleep    2s    reason=Need to wait to get value written in system

    @{values} =    veristand_api.Read Channels Values
    ...    ActualRPM
    ...    DesiredRPM
    ...    Engine Calculations/RPM Acceleration
    Builtin.Log    Channels values: ${values}
    Builtin.Should Not Be Equal As Numbers  first=${values[0]}    second=${0.0}
    Builtin.Should Be Equal As Numbers    first=${values[1]}    second=${0}
    Builtin.Should Not Be Equal As Numbers    first=${values[2]}    second=${0.0}

    veristand_api.Write Channels Values    DesiredRPM    1000.5
    BuiltIn.Sleep    1s    reason=Need to wait to get value written in system
    @{values} =    veristand_api.Read Channels Values    DesiredRPM
    Builtin.Should Be Equal As Numbers    first=${values[0]}    second=${1000.5}

    veristand_api.Write Channel Fault    channel_name=ActualRPM    value=0.5
    BuiltIn.Sleep    1s    reason=Need to wait to get value written in system
    ${act_rpm} =    veristand_api.Read Channel Value    channel_name=ActualRPM
    Builtin.Should Be Equal As Numbers    first=${act_rpm}    second=${0.5}

    veristand_api.Clear Channel Fault    channel_name=ActualRPM
    BuiltIn.Sleep    1s    reason=Need to wait to get value written in system
    ${act_rpm} =    veristand_api.Read Channel Value    ActualRPM
    ${min} =    BuiltIn.Convert To Number    900.0
    BuiltIn.Should Be True    ${act_rpm} > ${min}

Run Realtime Sequence In Engine Demo Project
    [Documentation]    Verifies veristand python API using Engine Demo project which is running on Windows.
    [Tags]    smoke    ate

    RealtimeSequences.Step Ramp
    ...    ramp_out_ch=DesiredRPM
    ...    init_value=${0}
    ...    final_value=${1000}
    ...    step_value=${500}
    ...    step_duration=${1}


*** Keywords ***
Setup Bench Local
    [Documentation]    Keyword for Suite setup to make sure bench is set OK

    BuiltIn.Wait Until Keyword Succeeds    3 times    500ms
    ...    Veristand Stop, Start And Deploy

Teardown Bench Local
    [Documentation]    Keyword for Suite setup to make sure bench is shut down OK

    veristand_api.Disconnect System And Undeploy Definition    undeploy=${True}
    veristand_api.Stop    timeout_s=${VERISTAND_STOP_TIMEOUT_S}
    # Make sure veristand-server process stops, sometimes it stays open after stop command
    veristand_api.Kill

Setup Test Local
    [Documentation]    Keyword to setup test

    ${gw_status} =    veristand_api.Get Deployment Status
    Builtin.Should Be Equal As Numbers    first=${gw_status['state']}    second=${1}
    Builtin.Should Be Equal As Strings
    ...    first=${gw_status['systemdefinition_file']}
    ...    second=${VERISTAND_SDF_DEMO_PATH}
    Log    Gatway status is: ${gw_status}

Teardown Test Local
    [Documentation]    Keyword to teardown test

    ${gw_status} =    veristand_api.Get Deployment Status
    Log    Gateway status is: ${gw_status}
    Builtin.Should Be Equal As Numbers    first=${gw_status['state']}    second=${1}
    Builtin.Should Be Equal As Strings
    ...    first=${gw_status['systemdefinition_file']}
    ...    second=${VERISTAND_SDF_DEMO_PATH}
    Check Veristand Alarms

Check Veristand Alarms
    [Documentation]    Checks alarms from Veristand and stops execution if fault alarms are ON.

    ${status} =    BuiltIn.Run Keyword And Return Status    veristand_api.Check Alarms

    IF    not ${status}
        BuiltIn.Fatal Error    msg=Alarms are ON, Test Execution needs to stop!
    END

Veristand Stop, Start And Deploy
    [Documentation]    Keyword to make sure NI Veristand is up and running and deployed.

    veristand_api.Stop       timeout_s=${VERISTAND_STOP_TIMEOUT_S}
    veristand_api.Start      timeout_s=${VERISTAND_START_TIMEOUT_S}
    veristand_api.Connect To System And Deploy Definition
    ...    sdf_path=${VERISTAND_SDF_DEMO_PATH}
    ...    deploy=${True}
    ...    timeout_s=${VERISTAND_SDF_DEPLOY_TIMEOUT_S}
