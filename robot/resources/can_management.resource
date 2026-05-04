*** Settings ***
Documentation       CAN related resource file for ATE test environment.

Resource            libraries_and_variables.resource


*** Keywords ***
Enable All ATE CAN Ports
    [Documentation]    Enables all ATE CAN port transceivers and selected outgoing frames.

    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN1_CAN1_PORT_SLEEP}    value=0
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN2_CAN2_PORT_SLEEP}    value=0
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN3_CAN3_PORT_SLEEP}    value=0
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN4_CAN4_PORT_SLEEP}    value=0
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN5_CAN5_PORT_SLEEP}    value=0
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN6_CAN6_PORT_SLEEP}    value=0

Disable All ATE CAN Ports
    [Documentation]    Disables all ATE CAN port transceivers and selected outgoing frames.
    ...                A port in Sleep mode does not transmit data until Sleep mode is released or until the port receives an incoming frame.
    ...                To totally disable outgoing frames, these same channels are also used to disable the actual frames.

    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN1_CAN1_PORT_SLEEP}    value=1
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN2_CAN2_PORT_SLEEP}    value=1
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN3_CAN3_PORT_SLEEP}    value=1
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN4_CAN4_PORT_SLEEP}    value=1
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN5_CAN5_PORT_SLEEP}    value=1
    VeristandApi.Write Channel Value    channel_name=${ALIASES_ATE_CAN6_CAN6_PORT_SLEEP}    value=1
