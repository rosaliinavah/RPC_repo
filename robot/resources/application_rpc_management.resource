*** Settings ***
Documentation       Paths to Codesys application variables
...                 Keywords to set variables and run commands in application

Resource            libraries_and_variables.resource


*** Variables ***
# APPLICATION INFO
${APP_INFO_POU} =           AppVersionInfo

${IO_DRIVER_POU} =          IoDriver
${POWER_SWITCH_POU} =       PowerSwitch

${REFOUT_POU} =             REFouts

${MEMORY_POU} =             Memory
${EPEC_SYSTEM_POU} =        EPEC_SYSTEM_LIB

# cSpell:disable
# CODESYS Library: EPEC_IODRV
# EPEC_IODRV.IoDrvStates
${IODRV_STATE_INIT} =                 0
${IODRV_STATE_HW_INIT_READY} =        1
${IODRV_STATE_CONFIGURATION} =        2
${IODRV_STATE_RUN} =                  3
${IODRV_STATE_DISABLED} =             4
${IODRV_STATE_SAFETY} =               5
# EPEC_IODRV.IoDrvTrigModes
${IODRV_TRIG_METHODS_RISING_EDGE} =   1
${IODRV_TRIG_METHODS_FALLING_EDGE} =  2
${IODRV_TRIG_METHODS_BOTH_EDGES} =    3
# EPEC_IODRV.IoDrvModes
${IODRV_MODE_DISABLED} =              0
${IODRV_MODE_PWM_DO} =                1
${IODRV_MODE_PWM_DIRECT} =            2
${IODRV_MODE_PI_1CH} =                26
${IODRV_MODE_PI_2CH} =                27
${IODRV_MODE_PI_RESET} =              28
${IODRV_MODE_PI_COUNT} =              29
${IODRV_MODE_PI_FREQUENCY} =          30
${IODRV_MODE_PI_PULSE_WIDTH} =        31
${IODRV_MODE_PI_PULSE_RATIO} =        32
${IODRV_MODE_PI_EDGE_TIME_STAMPS} =   33
${IODRV_MODE_AI_ENABLED} =            51
${IODRV_MODE_DI_ENABLED} =            76
${IODRV_MODE_DO_ENABLED} =            101
# EPEC_IODRV.DIAGNOSTIC_TASK_STATUS
${IODRV_DIAGNOSTIC_TASK_STATUS_EDIAGNOSTIC_STATUS_ERROR} =  3

# CODESYS Library: EPEC_SYSTEM
# No errors
${FW_ERR_OK} =                                                             SYSTEM_ERROR_CODES.FW_ERR_OK
# Not valid gate time value for gate time setting
${FW_ERR_IODRV_INVALID_GATE_TIME_VALUE} =                                  SYSTEM_ERROR_CODES.FW_ERR_IODRV_INVALID_GATE_TIME_VALUE
# Reseted channel for pulse input reset configuration is not configured to PI mode.
${FW_ERR_IODRV_RESETED_CHANNEL_NOT_CONFIGURED} =                           SYSTEM_ERROR_CODES.FW_ERR_IODRV_RESETED_CHANNEL_NOT_CONFIGURED
# Given reseted channel is not valid.
${FW_ERR_IODRV_ERR_CHN_NUMBER_NOT_VALID_RESETED_CHN} =                     SYSTEM_ERROR_CODES.FW_ERR_IODRV_ERR_CHN_NUMBER_NOT_VALID_RESETED_CHN
# Invalid triggering method for PI-channel
${FW_ERR_IODRV_INVALID_TRIGGERING_METHOD} =                                SYSTEM_ERROR_CODES.FW_ERR_IODRV_INVALID_TRIGGERING_METHOD
# Component has not been initialized properly.
${FW_ERR_UNINITIALIZED} =                                                  SYSTEM_ERROR_CODES.FW_ERR_UNINITIALIZED
# Parameter error for PWFM channel.
${FW_ERR_IODRV_HAL_PWFM_PARAMETER_ERROR} =                                 SYSTEM_ERROR_CODES.FW_ERR_IODRV_HAL_PWFM_PARAMETER_ERROR
# Error password system locked
${FW_ERR_PSW_SYS_LOCKED} =                                                 SYSTEM_ERROR_CODES.FW_ERR_PSW_SYS_LOCKED
# cSpell:enable

# IO Inputs POU
# ------------------------------AI-------------------------------
# B248-5-0 : AI Voltage 5V / Current
&{APP_IO_X1_27} =       pou=Inputs.IO_X1_27
&{APP_IO_X1_29} =       pou=Inputs.IO_X1_29
&{APP_IO_X1_42} =       pou=Inputs.IO_X1_42

# B248-3-0 : AI Voltage 5V / Current
&{APP_IO_X1_13} =       pou=Inputs.IO_X1_13
&{APP_IO_X1_14} =       pou=Inputs.IO_X1_14
&{APP_IO_X2_27} =       pou=Inputs.IO_X2_27
&{APP_IO_X2_28} =       pou=Inputs.IO_X2_28

# B248-3-1 : AI Voltage 5V
&{APP_IO_X2_19} =       pou=Inputs.IO_X2_19
&{APP_IO_X2_21} =       pou=Inputs.IO_X2_21
&{APP_IO_X2_22} =       pou=Inputs.IO_X2_22
&{APP_IO_X2_24} =       pou=Inputs.IO_X2_24
&{APP_IO_X2_25} =       pou=Inputs.IO_X2_25

# B248-4-4 : KL15
&{APP_IO_X3_32} =       pou=Inputs.IO_X3_32

# B285-0-3 : AI Voltage 5V / 10V / Current
&{APP_IO_X1_32} =       pou=Inputs.IO_X1_32        range_select=Yes
&{APP_IO_X1_33} =       pou=Inputs.IO_X1_33        range_select=Yes
&{APP_IO_X2_34} =       pou=Inputs.IO_X2_34        range_select=Yes
&{APP_IO_X2_35} =       pou=Inputs.IO_X2_35        range_select=Yes
&{APP_IO_X2_36} =       pou=Inputs.IO_X2_36        range_select=Yes
&{APP_IO_X2_37} =       pou=Inputs.IO_X2_37        range_select=Yes

# B285-1-0 : AI Voltage 5V / 10V / Current
&{APP_IO_X1_21} =       pou=Inputs.IO_X1_21        range_select=Yes
&{APP_IO_X1_22} =       pou=Inputs.IO_X1_22        range_select=Yes
&{APP_IO_X1_23} =       pou=Inputs.IO_X1_23        range_select=Yes
&{APP_IO_X2_30} =       pou=Inputs.IO_X2_30        range_select=Yes
&{APP_IO_X3_26} =       pou=Inputs.IO_X3_26        range_select=Yes
&{APP_IO_X3_27} =       pou=Inputs.IO_X3_27        range_select=Yes

# B286-0-1 : AI Voltage 5V
&{APP_IO_X3_29} =       pou=Inputs.IO_X3_29

# ------------------------------TI-------------------------------
# B286-3-0 : TI Voltage 5V with Pull-up / Gain selections
&{APP_IO_X1_09} =       pou=Inputs.IO_X1_9
&{APP_IO_X1_10} =       pou=Inputs.IO_X1_10
&{APP_IO_X1_11} =       pou=Inputs.IO_X1_11
&{APP_IO_X1_25} =       pou=Inputs.IO_X1_25
# B286-2-0 : TI Voltage 5V with Pull-up / Gain selections
&{APP_IO_X2_16} =       pou=Inputs.IO_X2_16
&{APP_IO_X2_32} =       pou=Inputs.IO_X2_32
&{APP_IO_X2_33} =       pou=Inputs.IO_X2_33

# ------------------------------PI-------------------------------
# B251-3-0 PI/DI Pull-up/Pull-down
&{APP_IO_X1_05} =       pou=Inputs.IO_X1_5        pi_type=eTPU     pull_up=Yes
&{APP_IO_X1_06} =       pou=Inputs.IO_X1_6        pi_type=eTPU     pull_up=Yes

# B251-4-0 PI/DI Pull-up/Pull-down
&{APP_IO_X2_03} =       pou=Inputs.IO_X2_3        pi_type=eMIOS    pull_up=Yes
&{APP_IO_X2_04} =       pou=Inputs.IO_X2_4        pi_type=eMIOS    pull_up=Yes
&{APP_IO_X2_05} =       pou=Inputs.IO_X2_5        pi_type=eMIOS    pull_up=Yes
&{APP_IO_X2_06} =       pou=Inputs.IO_X2_6        pi_type=eMIOS    pull_up=Yes

# B251-6-2 PI/DI Pull-up/Pull-down & SENT
&{APP_IO_X3_19} =       pou=Inputs.IO_X3_19       pi_type=eTPU     pull_up=Yes
&{APP_IO_X3_20} =       pou=Inputs.IO_X3_20       pi_type=eTPU     pull_up=Yes
&{APP_IO_X3_21} =       pou=Inputs.IO_X3_21       pi_type=eTPU     pull_up=Yes
&{APP_IO_X3_22} =       pou=Inputs.IO_X3_22       pi_type=eTPU     pull_up=Yes

# B291-0-0 PI/DI Pull-up/Pull-down & SENT
&{APP_IO_X3_23} =       pou=Inputs.IO_X3_23       pi_type=eTPU     pull_up=Yes
&{APP_IO_X3_24} =       pou=Inputs.IO_X3_24       pi_type=eTPU     pull_up=Yes

# B252-2-0 PI/DI Pull-down
&{APP_IO_X1_01} =       pou=Inputs.IO_X1_1        pi_type=eTPU
&{APP_IO_X1_02} =       pou=Inputs.IO_X1_2        pi_type=eTPU
&{APP_IO_X1_16} =       pou=Inputs.IO_X1_16       pi_type=eTPU
&{APP_IO_X1_17} =       pou=Inputs.IO_X1_17       pi_type=eTPU
&{APP_IO_X2_01} =       pou=Inputs.IO_X2_1        pi_type=eMIOS
&{APP_IO_X2_02} =       pou=Inputs.IO_X2_2        pi_type=eMIOS
&{APP_IO_X2_17} =       pou=Inputs.IO_X2_17       pi_type=eMIOS
&{APP_IO_X2_18} =       pou=Inputs.IO_X2_18       pi_type=eMIOS

# B252-3-0 PI/DI Pull-down
&{APP_IO_X1_03} =       pou=Inputs.IO_X1_3        pi_type=eTPU
&{APP_IO_X1_04} =       pou=Inputs.IO_X1_4        pi_type=eTPU

# ------------------------------PWM------------------------------
# B253-1-X PWM/DO/CM HS 2A, VM
&{APP_IO_X1_18} =       pou=Outputs.IO_X1_18
&{APP_IO_X1_19} =       pou=Outputs.IO_X1_19
&{APP_IO_X1_34} =       pou=Outputs.IO_X1_34
&{APP_IO_X1_35} =       pou=Outputs.IO_X1_35
&{APP_IO_X1_36} =       pou=Outputs.IO_X1_36
&{APP_IO_X1_37} =       pou=Outputs.IO_X1_37
&{APP_IO_X1_38} =       pou=Outputs.IO_X1_38
&{APP_IO_X1_39} =       pou=Outputs.IO_X1_39
&{APP_IO_X1_40} =       pou=Outputs.IO_X1_40
&{APP_IO_X1_41} =       pou=Outputs.IO_X1_41
&{APP_IO_X2_42} =       pou=Outputs.IO_X2_42
&{APP_IO_X2_43} =       pou=Outputs.IO_X2_43
&{APP_IO_X2_44} =       pou=Outputs.IO_X2_44
&{APP_IO_X2_45} =       pou=Outputs.IO_X2_45
&{APP_IO_X3_04} =       pou=Outputs.IO_X3_4
&{APP_IO_X3_05} =       pou=Outputs.IO_X3_5
&{APP_IO_X3_06} =       pou=Outputs.IO_X3_6
&{APP_IO_X3_07} =       pou=Outputs.IO_X3_7
&{APP_IO_X3_08} =       pou=Outputs.IO_X3_8
&{APP_IO_X3_09} =       pou=Outputs.IO_X3_9
&{APP_IO_X3_12} =       pou=Outputs.IO_X3_12
&{APP_IO_X3_13} =       pou=Outputs.IO_X3_13

# B253-2-X PWM/DO/CM HS 2A, VM or I/O GND
&{APP_IO_X3_14} =       pou=Outputs.IO_X3_14
&{APP_IO_X3_15} =       pou=Outputs.IO_X3_15

# B255-1-X PWM/DO HS 3A, VM & PVG
&{APP_IO_X2_12} =       pou=Outputs.IO_X2_12
&{APP_IO_X2_13} =       pou=Outputs.IO_X2_13
&{APP_IO_X2_14} =       pou=Outputs.IO_X2_14
&{APP_IO_X2_15} =       pou=Outputs.IO_X2_15
&{APP_IO_X3_44} =       pou=Outputs.IO_X3_44
&{APP_IO_X3_45} =       pou=Outputs.IO_X3_45

# B256-2-X PWM/DO HS 3A, VM
&{APP_IO_X1_15} =       pou=Outputs.IO_X1_15
&{APP_IO_X1_31} =       pou=Outputs.IO_X1_31
&{APP_IO_X2_31} =       pou=Outputs.IO_X2_31
&{APP_IO_X2_46} =       pou=Outputs.IO_X2_46

# B256-3-X PWM/DO HS 3A, VM or I/O GND
&{APP_IO_X2_09} =       pou=Outputs.IO_X2_9
&{APP_IO_X2_10} =       pou=Outputs.IO_X2_10
&{APP_IO_X3_31} =       pou=Outputs.IO_X3_31
&{APP_IO_X3_46} =       pou=Outputs.IO_X3_46

# B287-0-X PWM/DO HS/LS 4A, VM or I/O GND
&{APP_IO_X1_43} =       pou=Outputs.IO_X1_43
&{APP_IO_X1_44} =       pou=Outputs.IO_X1_44
&{APP_IO_X1_45} =       pou=Outputs.IO_X1_45
&{APP_IO_X1_46} =       pou=Outputs.IO_X1_46
&{APP_IO_X2_40} =       pou=Outputs.IO_X2_40
&{APP_IO_X2_41} =       pou=Outputs.IO_X2_41

# B288-0-X PWM/DO HS 3A, VM & PVG & AO 0-Uin
&{APP_IO_X3_42} =       pou=Outputs.IO_X3_42
&{APP_IO_X3_43} =       pou=Outputs.IO_X3_43

# AUXout
&{APP_IO_X8_02_AND_X9_02} =             pou=Outputs.IO_X8_02

# Diagnostics POU
# ----------------------------- AI Unsigned -------------------------------
&{APP_REFOUT_5V_MAIN_VOLTAGE} =         pou=Diagnostics.REFout_5V_main_voltage
&{APP_REFOUT_5V_REDUNDANT_VOLTAGE} =    pou=Diagnostics.REFout_5V_redundant_voltage
&{APP_REFOUT_10V_MAIN_VOLTAGE} =        pou=Diagnostics.REFout_10V_main_voltage
&{APP_REFOUT_10V_REDUNDANT_VOLTAGE} =   pou=Diagnostics.REFout_10V_redundant_voltage
&{APP_PCB_TEMPERATURE_1} =              pou=Diagnostics.PCB_temperature_1
&{APP_PCB_TEMPERATURE_2} =              pou=Diagnostics.PCB_temperature_2
&{APP_VOLTAGE_AFTER_SAFETY_SWITCH} =    pou=Diagnostics.Voltage_after_safety_switch
&{APP_VOLTAGE_BEFORE_SAFETY_SWITCH} =   pou=Diagnostics.Voltage_before_safety_switch
&{APP_SUPPLY_VOLTAGE} =                 pou=Diagnostics.Supply_voltage
&{APP_BSL_PIN_VOLTAGE} =                pou=Diagnostics.BSL_pin_voltage
# ------------------------------ AI Signed --------------------------------
&{APP_MCU_TEMPERATURE} =                pou=Diagnostics.MCU_temperature
&{APP_SBC_TEMPERATURE} =                pou=Diagnostics.SBC_temperature
&{APP_5V2_MEASUREMENT} =                pou=Diagnostics.Int_5V_2_measurement
&{APP_VBAT_3V3_MEASUREMENT} =           pou=Diagnostics.VBAT_3V3_measurement
&{APP_OUTPUT_CURRENT_SUM} =             pou=Diagnostics.Output_current_sum
# --------------------------------- DI ------------------------------------
&{APP_FACTORY_RESET} =                  pou=Diagnostics.Factory_reset
&{APP_SERVICE_MODE} =                   pou=Diagnostics.Service_mode


*** Keywords ***
IO Init AI Mode
    [Documentation]  Initializes analog input mode for voltage/current measurement
    [Arguments]    ${APP_IO_PIN}  ${mode}=${IODRV_MODE_AI_ENABLED}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Mode       value=${mode}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_Ai    value=${TRUE}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_Ai
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init AI Pull-up
    [Documentation]  Initializes analog input mode for pull-up voltage measurement
    [Arguments]    ${APP_IO_PIN}  ${mode}=${IODRV_MODE_AI_ENABLED}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_ModePullUp       value=${mode}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_Ai_PullUp    value=${TRUE}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_Ai_PullUp
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init AI Mean Filtering Samples
    [Documentation]  Initializes nbr of filtering samples for analog input
    [Arguments]    ${APP_IO_PIN}    ${nbr_of_samples}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_FilterSamples         value=${nbr_of_samples}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_MeanFiltering    value=${TRUE}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_MeanFiltering
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init AI Gain
    [Documentation]  Initializes analog input gain selection
    ...    - Gain 0, PU 0 = thermistor mode 40-100000 ohm (2k3 optimized)
    ...    - Gain 0, PU 1 = thermistor mode 40-100000 ohm (15k optimized)
    ...    - Gain 1, PU 0 = thermistor mode 0-300 ohm
    ...    - Gain 1, PU 1 = thermistor mode 700-2200 ohm

    [Arguments]    ${app_io_pin}    ${gain}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_GainSelect            value=${gain}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_GainSelection    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_GainSelection
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init AI Pull-up Selection
    [Documentation]  Initializes analog input pull-up selection
    ...    - Gain 0, PU 0 = thermistor mode 40-100000 ohm (2k3 optimized)
    ...    - Gain 0, PU 1 = thermistor mode 40-100000 ohm (15k optimized)
    ...    - Gain 1, PU 0 = thermistor mode 0-300 ohm
    ...    - Gain 1, PU 1 = thermistor mode 700-2200 ohm

    [Arguments]    ${app_io_pin}    ${pull_up_select}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_PullUpSelect          value=${pull_up_select}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_PullUpSelection  value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_PullUpSelection
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init AI 5V Range
    [Documentation]  Sets analog input to 5V range
    [Arguments]    ${APP_IO_PIN}

    IO Init AI Range    app_io_pin=${APP_IO_PIN}    range_5v=${TRUE}

IO Init AI 10V Range
    [Documentation]  Sets analog input to 10V range
    [Arguments]    ${APP_IO_PIN}

    IO Init AI Range    app_io_pin=${APP_IO_PIN}    range_5v=${FALSE}

IO Init AI Range
    [Documentation]  Sets analog input to 10V range
    [Arguments]    ${app_io_pin}   ${range_5v}
    [Tags]    robot:private

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_VoltageSelect_5V         value=${range_5v}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_VoltageSelection    value=${TRUE}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_VoltageSelection
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init AI Voltage Type
    [Documentation]  Sets analog input type to measure voltage
    [Arguments]    ${APP_IO_PIN}

    IO Init AI Type  app_io_pin=${APP_IO_PIN}    type_ma=${FALSE}

IO Init AI Current Type
    [Documentation]  Sets analog input type to measure current
    [Arguments]    ${APP_IO_PIN}

    IO Init AI Type  app_io_pin=${APP_IO_PIN}    type_ma=${TRUE}

IO Init AI Type
    [Documentation]  Sets analog input type to measure voltage or current
    [Arguments]    ${app_io_pin}    ${type_ma}
    [Tags]    robot:private

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_TypeSelect_mA         value=${type_ma}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_TypeSelection    value=${TRUE}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_TypeSelection
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

AI Read Unscaled Value
    [Documentation]  Reads analog input unscaled value from application
    [Arguments]    ${APP_IO_PIN}

    ${value} =    CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Ai_Unscaled
    RETURN    ${value}

AI Read Unscaled Pull-Up Value
    [Documentation]  Reads analog input unscaled pull-up value from application
    [Arguments]      ${APP_IO_PIN}

    ${value} =       CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Ai_PullUp_Unscaled
    RETURN           ${value}

IO Set PI Triggering Method
    [Documentation]  Sets the PI triggering method
    [Arguments]    ${APP_IO_PIN}  ${triggering_method}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_TriggeringMethod    value=${triggering_method}

IO Init PI Mode 1Ch
    [Documentation]  Initializes pulse input to 1CH mode
    [Arguments]    ${APP_IO_PIN}    ${expected_error_code}=${FW_ERR_OK}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Mode       value=${IODRV_MODE_PI_1CH}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_Pi    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_Pi
    BuiltIn.Should Be Equal    ${error_code}   ${expected_error_code}

IO Init PI Mode 1Ch Reset
    [Documentation]  Initializes pulse input to Reset mode
    [Arguments]      ${APP_IO_PIN}    ${reset_channel}    ${reset_value}    ${expected_error_code}=${FW_ERR_OK}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Mode            value=${IODRV_MODE_PI_RESET}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_ResetChannel    value=${reset_channel}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_ResetValue      value=${reset_value}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_PiReset    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_PiReset

    BuiltIn.Should Be Equal    ${error_code}  ${expected_error_code}

IO Init PI Mode 1Ch Frequency
    [Documentation]  Initializes pulse input to 1CH Frequency mode
    [Arguments]    ${APP_IO_PIN}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Mode       value=${IODRV_MODE_PI_FREQUENCY}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_Pi    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_Pi
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init PI Mode 1Ch Count
    [Documentation]  Initializes pulse input to 1CH Pulse Count mode
    [Arguments]    ${APP_IO_PIN}  ${expected_error_code}=${FW_ERR_OK}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Mode       value=${IODRV_MODE_PI_COUNT}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_Pi    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_Pi
    BuiltIn.Should Be Equal    ${error_code}  ${expected_error_code}

IO Init PI Mode 1Ch Width
    [Documentation]  Initializes pulse input to 1CH Pulse Width mode
    [Arguments]    ${APP_IO_PIN}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Mode       value=${IODRV_MODE_PI_PULSE_WIDTH}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_Pi    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_Pi
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init PI Mode 1Ch Ratio
    [Documentation]  Initializes pulse input to 1CH Pulse Ratio mode
    [Arguments]    ${app_io_pin}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Mode       value=${IODRV_MODE_PI_PULSE_RATIO}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_Pi    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_Pi
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init PI Mode 1Ch Edge Timestamps
    [Documentation]  Initializes pulse input to 1CH Edge Timestamps mode
    [Arguments]    ${app_io_pin}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Mode       value=${IODRV_MODE_PI_EDGE_TIME_STAMPS}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_Pi    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_Pi
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init PI Mode 2Ch
    [Documentation]  Initializes pulse inputs to 2CH mode
    [Arguments]      ${app_io_pin}    ${ch_b_str}    ${expected_error_code}=${FW_ERR_OK}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Mode        value=${IODRV_MODE_PI_2CH}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Channel_B   value=${ch_b_str}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_Pi2Ch  value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_Pi2Ch

    BuiltIn.Should Be Equal    ${error_code}  ${expected_error_code}

IO Init PI Gate Time
    [Documentation]  Initializes pulse input gate time
    [Arguments]    ${APP_IO_PIN}  ${gate_time}=100  ${expected_error_code}=${FW_ERR_OK}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_GateTime         value=${gate_time}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_GateTime    value=${TRUE}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_GateTime
    BuiltIn.Should Be Equal    ${error_code}  ${expected_error_code}

IO Init PI Pull-up
    [Documentation]  Initializes pulse input pull-up
    [Arguments]    ${APP_IO_PIN}  ${enable_pull_up}=${False}

    # Pull-up selection works inverted:  False=Pull-up enabled, True=Pull-up disabled
    ${set_pull_up} =  Evaluate  not ${enable_pull_up}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_PullUpSelect            value=${set_pull_up}
    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Init_PullUpSelection    value=${TRUE}

    ${error_code} =  CodesysRpcClient.Read Variable     ${APP_IO_PIN.pou}.o_ErrorCode_Init_PullUpSelection
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Read PI Mode Init Error Code
    [Documentation]  Reads initialization function error code
    [Arguments]    ${app_io_pin}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_Pi
    RETURN  ${error_code}

PI Read Unscaled Frequency Value
    [Documentation]  Reads pulse input unscaled frequency value (mHz) from application
    [Arguments]    ${APP_IO_PIN}

    ${value} =    CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Pi_Frequency
    RETURN    ${value}

PI Read Unscaled Ratio Value
    [Documentation]  Reads pulse input unscaled ratio value (0.01%) from application
    [Arguments]    ${APP_IO_PIN}

    ${value} =    CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Pi_PulseRatio
    RETURN    ${value}

PI Read Unscaled Pulse Width Value
    [Documentation]  Reads pulse input unscaled ratio value (uS) from application
    [Arguments]    ${APP_IO_PIN}

    ${value} =    CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Pi_PulseWidth
    RETURN    ${value}

PI Read Count Value
    [Documentation]  Reads pulse count value from application
    [Arguments]    ${APP_IO_PIN}

    ${value} =    CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Pi_PulseCount
    RETURN    ${value}

PI Read DI Status
    [Documentation]  Reads DI status from application
    [Arguments]    ${APP_IO_PIN}

    ${value} =    CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Pi_DiStatus    ret_type=bool
    RETURN    ${value}

PI Read Unscaled Rising Timestamp
    [Documentation]  Reads Rising timestamp from application
    [Arguments]    ${APP_IO_PIN}

    ${value} =    CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Pi_RisingTimestamp
    RETURN    ${value}

PI Read Unscaled Falling Timestamp
    [Documentation]  Reads falling timestamp from application
    [Arguments]    ${APP_IO_PIN}

    ${value} =    CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Pi_FallingTimestamp
    RETURN    ${value}

PI Read Unscaled Rising Timestamp Delta Time
    [Documentation]  Reads calculated rising timestamp delta time from application
    [Arguments]    ${APP_IO_PIN}

    ${value} =    CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Pi_RisingTimestampDeltaTime
    RETURN    ${value}

PI Read Unscaled Falling Timestamp Delta Time
    [Documentation]  Reads calculated falling timestamp delta time from application
    [Arguments]    ${APP_IO_PIN}

    ${value} =    CodesysRpcClient.Read Variable    ${APP_IO_PIN.pou}.o_Pi_FallingTimestampDeltaTime
    RETURN    ${value}

IO Init PWM HS Direct Mode
    [Documentation]  Initializes PWM HS output to PWM Direct mode
    [Arguments]      ${app_io_pin}  ${mode}=${IODRV_MODE_PWM_DIRECT}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Mode           value=${mode}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_PWM_HS    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_PWM_HS
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init PWM LS Direct Mode
    [Documentation]  Initializes PWM LS output to PWM Direct mode
    [Arguments]      ${app_io_pin}  ${mode}=${IODRV_MODE_PWM_DIRECT}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Mode           value=${mode}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_PWM_LS    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_PWM_LS
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init PWM HS DO Mode
    [Documentation]  Initializes PWM HS output to PWM DO mode
    [Arguments]      ${app_io_pin}  ${mode}=${IODRV_MODE_PWM_DO}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Mode           value=${mode}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_PWM_HS    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_PWM_HS
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init PWM LS DO Mode
    [Documentation]  Initializes PWM LS output to PWM DO mode
    [Arguments]      ${app_io_pin}  ${mode}=${IODRV_MODE_PWM_DO}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Mode           value=${mode}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_PWM_LS    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_PWM_LS
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init PWM Current Measurement
    [Documentation]  Initializes PWM current measurement
    [Arguments]      ${app_io_pin}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_CurrentMeasurement         value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_CurrentMeasurement
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init PWM Voltage Measurement
    [Documentation]  Initializes PWM voltage measurement
    [Arguments]      ${app_io_pin}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_VoltageMeasurement         value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_VoltageMeasurement
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

IO Init PWM Overcurrent Configuration
    [Documentation]  Initializes PWM overcurrent configuration
    ...              - Overcurrent limit percent = Overcurrent limit value in % of maximum hardware limit
    ...              - Delay = Overcurrent delay in ms
    [Arguments]      ${app_io_pin}    ${overcurrent_limit_percent}=100    ${delay}=100    ${expected_error_code}=${FW_ERR_OK}

    # Overcurrent limit value in [%] of maximum hardware limit
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_OverCurrentLimitPercent          value=${overcurrent_limit_percent}
    # Overcurrent delay in ms
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_OverCurrentDelay                 value=${delay}
    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_Init_OverCurrentConfiguration    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_io_pin.pou}.o_ErrorCode_Init_OvercurrentConfiguration
    BuiltIn.Should Be Equal    ${error_code}  ${expected_error_code}

PWM HS Set Ratio
    [Documentation]  Sets PWM HS ratio value
    [Arguments]      ${app_io_pin}  ${ratio}=0

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_PWM_Ratio_HS                     value=${ratio}

PWM LS Set Ratio
    [Documentation]  Sets PWM LS ratio value
    [Arguments]      ${app_io_pin}  ${ratio}=0

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_PWM_Ratio_LS                     value=${ratio}

PWM HS Set Frequency
    [Documentation]  Sets PWM HS frequency value
    [Arguments]      ${app_io_pin}  ${frequency}=0

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_PWM_Frequency_HS                 value=${frequency}

PWM LS Set Frequency
    [Documentation]  Sets PWM LS frequency value
    [Arguments]      ${app_io_pin}  ${frequency}=0

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_PWM_Frequency_LS                 value=${frequency}

PWM HS Set DO Control
    [Documentation]  Sets PWM HS DO control
    [Arguments]      ${app_io_pin}    ${state}=${False}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_PWM_DO_Control_HS                value=${state}

PWM LS Set DO Control
    [Documentation]  Sets PWM LS DO control
    [Arguments]      ${app_io_pin}    ${state}=${False}

    CodesysRpcClient.Write Variable    ${app_io_pin.pou}.i_PWM_DO_Control_LS                value=${state}

PWM HS Read Unscaled Current Value
    [Documentation]  Reads PWM output unscaled current measurement (mA) from application
    [Arguments]      ${app_io_pin}

    ${value} =    CodesysRpcClient.Read Variable    ${app_io_pin.pou}.o_PWM_Current_measurement
    RETURN    ${value}

PWM Read Unscaled Voltage Value
    [Documentation]  Reads PWM output unscaled voltage measurement from application
    [Arguments]      ${app_io_pin}

    ${value} =    CodesysRpcClient.Read Variable    ${app_io_pin.pou}.o_PWM_Voltage_measurement
    RETURN    ${value}

PWM HS Read Channel Status
    [Documentation]  Reads PWM HS channel status from application
    [Arguments]      ${app_io_pin}

    ${value} =    CodesysRpcClient.Read Variable    ${app_io_pin.pou}.o_PWM_Status_HS
    RETURN    ${value}

PWM LS Read Channel Status
    [Documentation]  Reads PWM LS channel status from application
    [Arguments]      ${app_io_pin}

    ${value} =    CodesysRpcClient.Read Variable    ${app_io_pin.pou}.o_PWM_Status_LS
    RETURN    ${value}

Reset Application Pou
    [Documentation]  Resets application POU variables. The actual variables to be reset are defined inside specific POU.
    [Arguments]    ${APP_IO_PIN}

    CodesysRpcClient.Write Variable    ${APP_IO_PIN.pou}.i_Reset    value=${TRUE}

Set Io-Driver To Configuration Mode
    [Documentation]    Call IoDrvSetState function to set configuration mode

    CodesysRpcClient.Write Variable    ${IO_DRIVER_POU}.i_IoDrvSetState    value=${IODRV_STATE_CONFIGURATION}
    ${error_code} =  CodesysRpcClient.Read Variable     ${IO_DRIVER_POU}.o_ErrorCode_IoDrvSetState
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

Set Io-Driver To Run Mode
    [Documentation]    Call IoDrvSetState function to set run mode

    CodesysRpcClient.Write Variable    ${IO_DRIVER_POU}.i_IoDrvSetState    value=${IODRV_STATE_RUN}

    ${error_code} =  CodesysRpcClient.Read Variable     ${IO_DRIVER_POU}.o_ErrorCode_IoDrvSetState
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

Io-Driver Get State
    [Documentation]    Call IoDrvGetDiagnostic function to get run state

    CodesysRpcClient.Write Variable    ${IO_DRIVER_POU}.i_IoDrvGetState    value=${True}

    ${state} =  CodesysRpcClient.Read Variable     ${IO_DRIVER_POU}.o_IoDrvState
    RETURN    ${state}

Io-Driver Get Diagnostic Status
    [Documentation]    Call GetDiagnosticStatus function to get DIAGNOSTIC_TASK_STATUS

    CodesysRpcClient.Write Variable    ${IO_DRIVER_POU}.i_IoDrvGetDiagnosticStatus    value=${True}

    ${state} =  CodesysRpcClient.Read Variable     ${IO_DRIVER_POU}.o_DiagnosticStatus
    RETURN    ${state}

Diagnostics Init Analog Measurement
    [Documentation]  Initializes analog diagnostic measurement
    [Arguments]    ${app_pou}  ${mode}=${IODRV_MODE_AI_ENABLED}

    CodesysRpcClient.Write Variable    ${app_pou.pou}.i_Mode       value=${mode}
    CodesysRpcClient.Write Variable    ${app_pou.pou}.i_Init_Ai    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_pou.pou}.o_ErrorCode_Init_Ai
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

Diagnostics Init Digital Measurement
    [Documentation]  Initializes digital diagnostic measurement
    [Arguments]    ${app_pou}  ${mode}=${IODRV_MODE_DI_ENABLED}

    CodesysRpcClient.Write Variable    ${app_pou.pou}.i_Mode       value=${mode}
    CodesysRpcClient.Write Variable    ${app_pou.pou}.i_Init_Di    value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${app_pou.pou}.o_ErrorCode_Init_Di
    BuiltIn.Should Be Equal    ${error_code}  ${FW_ERR_OK}

Diagnostics Read Unscaled Value
    [Documentation]  Reads analog input unscaled value from application
    [Arguments]    ${app_pou}

    ${value} =    CodesysRpcClient.Read Variable    ${app_pou.pou}.o_Ai_Unscaled
    RETURN    ${value}

Diagnostics Read Digital Value
    [Documentation]  Reads digital input value from application
    [Arguments]    ${app_pou}

    ${value} =    CodesysRpcClient.Read Variable    ${app_pou.pou}.o_Di
    RETURN    ${value}

Diagnostics Read Output Current Sum Value
    [Documentation]  Reads PWM output current sum value from application

    ${value} =    CodesysRpcClient.Read Variable    ${APP_OUTPUT_CURRENT_SUM.pou}.o_Ai_Unscaled
    RETURN    ${value}

Run Power Switch Startup Test
    [Documentation]    Call PowerSwitchStartupTest function
    [Arguments]      ${sleep_s}=0.2s   ${expected_error_code}=${FW_ERR_OK}

    CodesysRpcClient.Write Variable    ${POWER_SWITCH_POU}.i_PowerSwitchStartupTest    value=${True}

    BuiltIn.Sleep    ${sleep_s}

    ${error_code} =  CodesysRpcClient.Read Variable     ${POWER_SWITCH_POU}.o_ErrorCode_PowerSwitchStartupTest
    BuiltIn.Should Be Equal    ${error_code}  ${expected_error_code}

Activate Power Switch
    [Documentation]    Call PowerSwitchSet function to activate the power switch (safety switch)
    [Arguments]      ${power_switch_nbr}=${1}  ${expected_error_code}=${FW_ERR_OK}

    Set Power Switch State    power_switch_state=${1}      power_switch_nbr=${power_switch_nbr}    expected_error_code=${expected_error_code}

De-Activate Power Switch
    [Documentation]    Call PowerSwitchSet function to de-activate the power switch (safety switch)
    [Arguments]      ${power_switch_nbr}=${1}  ${expected_error_code}=${FW_ERR_OK}

    Set Power Switch State    power_switch_state=${0}      power_switch_nbr=${power_switch_nbr}    expected_error_code=${expected_error_code}

Set Power Switch State
    [Documentation]    Call PowerSwitchSet function
    ...
    ...                power_switch_state: 0 = de-activated, 1 = activated
    ...                power_switch_nbr:   0 = all, 1 = first, 2 = second
    # TODO Test suite for safety switch must be done. When calling with power_switch_nbr=0, FW returns error.
    [Arguments]      ${power_switch_state}=${0}  ${power_switch_nbr}=${0}  ${expected_error_code}=${FW_ERR_OK}
    [Tags]             robot:private

    CodesysRpcClient.Write Variable    ${POWER_SWITCH_POU}.i_PowerSwitchNbr            value=${power_switch_nbr}
    CodesysRpcClient.Write Variable    ${POWER_SWITCH_POU}.i_PowerSwitchState          value=${power_switch_state}
    CodesysRpcClient.Write Variable    ${POWER_SWITCH_POU}.i_PowerSwitchSet            value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${POWER_SWITCH_POU}.o_ErrorCode_PowerSwitchSet
    BuiltIn.Should Be Equal    ${error_code}  ${expected_error_code}

Get Application Project Information
    [Documentation]    Gets application project information

    ${project_name} =     CodesysRpcClient.Read Variable     ${APP_INFO_POU}.o_StrProjectName
    ${project_title} =    CodesysRpcClient.Read Variable     ${APP_INFO_POU}.o_StrTitle
    ${project_version} =  CodesysRpcClient.Read Variable     ${APP_INFO_POU}.o_StrVersion
    ${device_name} =      CodesysRpcClient.Read Variable     ${APP_INFO_POU}.o_StrDeviceName
    ${device_version} =   CodesysRpcClient.Read Variable     ${APP_INFO_POU}.o_StrDeviceVersion

    ${project_info} =  BuiltIn.Create List  ${project_name}  ${project_title}  ${project_version}  ${device_name}  ${device_version}

    RETURN  ${project_info}

Get Application Project Name
    [Documentation]    Gets application project name

    ${project_name} =     CodesysRpcClient.Read Variable     ${APP_INFO_POU}.o_StrProjectName

    RETURN  ${project_name}

Activate Refouts 5V
    [Documentation]     Call SystemControlRef function to activate the Refouts
    [Arguments]         ${expected_error_code}=${FW_ERR_OK}

    Set Refouts 5V State     ref_state=${True}   expected_error_code=${expected_error_code}

De-Activate Refouts 5V
    [Documentation]     Call SystemControlRef function to de-activate the Refouts
    [Arguments]         ${expected_error_code}=${FW_ERR_OK}

    Set Refouts 5V State     ref_state=${False}   expected_error_code=${expected_error_code}

Set Refouts 5V State
    [Documentation]     Call SystemControlRef function to set the Refouts
    ...
    ...                ref_state: False = de-activated, True = activated
    [Arguments]        ${ref_state}=${False}   ${expected_error_code}=${FW_ERR_OK}
    [Tags]             robot:private

    CodesysRpcClient.Write Variable     ${REFOUT_POU}.i_REFout5V_State     value=${ref_state}
    CodesysRpcClient.Write Variable     ${REFOUT_POU}.i_REFout5V_Set       value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${REFOUT_POU}.o_ErrorCode_SystemControlRef_5V
    BuiltIn.Should Be Equal    ${error_code}  ${expected_error_code}

Activate Refouts 10V
    [Documentation]     Call SystemControlRef function to activate the Refouts
    [Arguments]         ${expected_error_code}=${FW_ERR_OK}

    Set Refouts 10V State     ref_state=${True}   expected_error_code=${expected_error_code}

De-Activate Refouts 10V
    [Documentation]     Call SystemControlRef function to de-activate the Refouts
    [Arguments]         ${expected_error_code}=${FW_ERR_OK}

    Set Refouts 10V State     ref_state=${False}   expected_error_code=${expected_error_code}

Set Refouts 10V State
    [Documentation]     Call SystemControlRef function to set the Refouts
    ...
    ...                ref_state: False = de-activated, True = activated
    [Arguments]        ${ref_state}=${False}   ${expected_error_code}=${FW_ERR_OK}
    [Tags]             robot:private

    CodesysRpcClient.Write Variable     ${REFOUT_POU}.i_REFout10V_State     value=${ref_state}
    CodesysRpcClient.Write Variable     ${REFOUT_POU}.i_REFout10V_Set       value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${REFOUT_POU}.o_ErrorCode_SystemControlRef_10V
    BuiltIn.Should Be Equal    ${error_code}  ${expected_error_code}

Activate Refouts Main Switch
    [Documentation]     Call SystemControlRef function to activate the Refouts
    [Arguments]         ${expected_error_code}=${FW_ERR_OK}

    Set Refouts Main Switch State     ref_state=${True}   expected_error_code=${expected_error_code}

De-Activate Refouts Main Switch
    [Documentation]     Call SystemControlRef function to de-activate the Refouts
    [Arguments]         ${expected_error_code}=${FW_ERR_OK}

    Set Refouts Main Switch State     ref_state=${False}   expected_error_code=${expected_error_code}

Set Refouts Main Switch State
    [Documentation]     Call SystemControlRefoutSwitch function to set the Refouts Switch
    ...
    ...                ref_state: False = de-activated, True = activated
    [Arguments]        ${ref_state}=${False}   ${expected_error_code}=${FW_ERR_OK}
    [Tags]             robot:private

    CodesysRpcClient.Write Variable     ${REFOUT_POU}.i_REFoutMainSwitch_State     value=${ref_state}
    CodesysRpcClient.Write Variable     ${REFOUT_POU}.i_REFoutMainSwitch_Set       value=${True}

    ${error_code} =  CodesysRpcClient.Read Variable     ${REFOUT_POU}.o_ErrorCode_SystemControlRefoutSwitch
    BuiltIn.Should Be Equal    ${error_code}  ${expected_error_code}

Check Whether Safe State Is Activated
    [Documentation]     Check Whether Safe State Is Activated
    [Arguments]         ${safe_activated}

    ${io_driver_diagnostic_status} =  Io-Driver Get Diagnostic Status

    IF    ${safe_activated}
        BuiltIn.Should Be Equal        ${io_driver_diagnostic_status}  ${IODRV_DIAGNOSTIC_TASK_STATUS_EDIAGNOSTIC_STATUS_ERROR}
    ELSE
        BuiltIn.Should Not Be Equal    ${io_driver_diagnostic_status}  ${IODRV_DIAGNOSTIC_TASK_STATUS_EDIAGNOSTIC_STATUS_ERROR}
    END

Read NVRAM Size
    [Documentation]     Call NVRAMGETSIZE function to get DUT NVRAM size.
    ...                 Index = NvRAM index which memory information is requested. Default value = 0
    [Arguments]         ${index}=${0}

    CodesysRpcClient.Write Variable               ${MEMORY_POU}.NvramIndex       value=${index}
    CodesysRpcClient.Write Variable               ${MEMORY_POU}.NvramGetSize     value=${True}
    ${size} =  CodesysRpcClient.Read Variable     ${MEMORY_POU}.NvramSize

    RETURN  ${size}

Password Unlock
    [Documentation]     Call PasswordUnlock function to unlock DUT.
    ...                 - DUT password is given as an argument.
    [Arguments]         ${password}=${PASSWORD}

    CodesysRpcClient.Write Variable               ${EPEC_SYSTEM_POU}.i_CurrentPassword      value='${password}'
    CodesysRpcClient.Write Variable               ${EPEC_SYSTEM_POU}.i_UnlockDevice         value=${True}
    ${status} =  CodesysRpcClient.Read Variable   ${EPEC_SYSTEM_POU}.o_ErrorCode_PasswordUnlock

    RETURN  ${status}

Password Change
    [Documentation]     Call PasswordChange function to change DUT password.
    ...                 - NOTE: DUT is not unlocked during this keyword.
    [Arguments]         ${current_password}=${EMPTY}    ${new_password}=${EMPTY}

    CodesysRpcClient.Write Variable               ${EPEC_SYSTEM_POU}.i_CurrentPassword      value='${current_password}'
    CodesysRpcClient.Write Variable               ${EPEC_SYSTEM_POU}.i_NewPassword          value='${new_password}'
    CodesysRpcClient.Write Variable               ${EPEC_SYSTEM_POU}.i_ChangePassword       value=${True}

    ${status} =  CodesysRpcClient.Read Variable   ${EPEC_SYSTEM_POU}.o_ErrorCode_PasswordChange

    RETURN  ${status}

System Parameters Restore
    [Documentation]     Call SystemParametersRestore function to restore DUT system parameters.
    ...                 - NOTE: DUT is not unlocked during this keyword.

    CodesysRpcClient.Write Variable               ${EPEC_SYSTEM_POU}.i_RestoreSystemParameters       value=${True}
    BuiltIn.Sleep    1s    reason=Wait DUT FW to make restore
    ${status} =  CodesysRpcClient.Read Variable   ${EPEC_SYSTEM_POU}.o_ErrorCode_RestoreParameters

    RETURN  ${status}

System Parameters Save
    [Documentation]     Call SystemParametersSave function to save DUT system parameters.
    ...                 - NOTE: DUT is not unlocked during this keyword.

    CodesysRpcClient.Write Variable               ${EPEC_SYSTEM_POU}.i_SaveSystemParameters       value=${True}
    BuiltIn.Sleep    1s    reason=Wait DUT FW to make save
    ${status} =  CodesysRpcClient.Read Variable   ${EPEC_SYSTEM_POU}.o_ErrorCode_SaveParameters

    RETURN  ${status}
