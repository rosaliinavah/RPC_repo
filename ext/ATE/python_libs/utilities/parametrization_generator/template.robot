*** Settings ***
Documentation       DESCRIPTION_BY_GENERATOR
...                 Generated resource to parametrize EPEC product via CANOpen protocol.

Resource            libraries_and_variables.resource
Resource            dut.resource


*** Keywords ***
Configure PDO_PREFIX_BY_GENERATOR PDOs
    [Documentation]    Configures PDOs with possible sub indexes using CANOpen

    KEYWORD_CALLS_BY_GENERATOR

Configure PDO
    [Documentation]    Keyword to configure PDO with possible sub indexes using CANOpen
    [Arguments]
    ...    @{pdo_map_values}
    ...    ${node_id}=0
    ...    ${cob_id_decimal}=0
    ...    ${pdo_com_parameter_name}=None
    ...    ${pdo_mapping_parameter_name}=None
    ...    ${transmission_type}=255
    ...    ${inhibit_time}=100
    ...    ${event_timer}=300
    ...    ${sync_start_value}

    ${nbr_of_sub_indexes} =   BuiltIn.Get Length   ${pdo_map_values}

    Disable Communication Parameter Cob-id
    ...    node_id=${node_id}
    ...    pdo_com_parameter_name=${pdo_com_parameter_name}

    IF  ${nbr_of_sub_indexes} > 0
        Clear Mappings
        ...    node_id=${node_id}
        ...    pdo_mapping_parameter_name=${pdo_mapping_parameter_name}

        Configure Pdo Mapping Parameter
        ...    @{pdo_map_values}
        ...    node_id=${node_id}
        ...    pdo_mapping_parameter_name=${pdo_mapping_parameter_name}

        Set Number Of Mappings
        ...    node_id=${node_id}
        ...    pdo_mapping_parameter_name=${pdo_mapping_parameter_name}
        ...    nbr_of_sub_indexes=${nbr_of_sub_indexes}

        Configure Pdo Communication Parameters
        ...    node_id=${node_id}
        ...    pdo_com_parameter_name=${pdo_com_parameter_name}
        ...    cob_id_decimal=${cob_id_decimal}
        ...    transmission_type=${transmission_type}
        ...    inhibit_time=${inhibit_time}
        ...    event_timer=${event_timer}
        ...    sync_start_value=${sync_start_value}
    END

Disable Communication Parameter Cob-id
    [Documentation]     Disable Communication Parameter Cob-id
    [Arguments]         ${node_id}  ${pdo_com_parameter_name}

    BuiltIn.Log    Disable CobId of configured PDO
    ${disable_value} =  BuiltIn.Convert To Integer    0x80000000
    DeviceUnderTest.Write Sdo
    ...    node_id=${node_id}
    ...    index_name=${pdo_com_parameter_name}
    ...    sub_name=1
    ...    data=${disable_value}

Clear Mappings
    [Documentation]     Clear mappings by writing 0 to sub0 of mapping index
    [Arguments]         ${node_id}  ${pdo_mapping_parameter_name}

    DeviceUnderTest.Write Sdo
    ...    node_id=${node_id}
    ...    index_name=${pdo_mapping_parameter_name}
    ...    sub_name=0
    ...    data=0

Set Number Of Mappings
    [Documentation]     Set the number of mapping to sub0 of mapping index
    [Arguments]         ${node_id}  ${pdo_mapping_parameter_name}  ${nbr_of_sub_indexes}

    DeviceUnderTest.Write Sdo
    ...    node_id=${node_id}
    ...    index_name=${pdo_mapping_parameter_name}
    ...    sub_name=0
    ...    data=${nbr_of_sub_indexes}

Configure Pdo Communication Parameters
    [Documentation]    Configure PDO communication parameters such as
    ...                transmission type, inhibit time, event timer and sync start time.
    [Arguments]
    ...    ${node_id}
    ...    ${pdo_com_parameter_name}
    ...    ${cob_id_decimal}
    ...    ${transmission_type}
    ...    ${inhibit_time}
    ...    ${event_timer}
    ...    ${sync_start_value}

    BuiltIn.Log    Set Transmission Type
    DeviceUnderTest.Write Sdo
    ...    node_id=${node_id}
    ...    index_name=${pdo_com_parameter_name}
    ...    sub_name=2
    ...    data=${transmission_type}

    BuiltIn.Log    Set Inhibit Time
    DeviceUnderTest.Write Sdo
    ...    node_id=${node_id}
    ...    index_name=${pdo_com_parameter_name}
    ...    sub_name=3
    ...    data=${inhibit_time}

    BuiltIn.Log    Set Event Timer
    DeviceUnderTest.Write Sdo
    ...    node_id=${node_id}
    ...    index_name=${pdo_com_parameter_name}
    ...    sub_name=5
    ...    data=${event_timer}

    BuiltIn.Log    Set SYNC start value
    IF  '${sync_start_value}' != ''
        DeviceUnderTest.Write Sdo
        ...    node_id=${node_id}
        ...    index_name=${pdo_com_parameter_name}
        ...    sub_name=6
        ...    data=${sync_start_value}
    END

    BuiltIn.Log    Set Cob-Id
    DeviceUnderTest.Write Sdo
    ...    node_id=${node_id}
    ...    index_name=${pdo_com_parameter_name}
    ...    sub_name=1
    ...    data=${cob_id_decimal}

Configure Pdo Mapping Parameter
    [Documentation]  Configure Pdo Mapping Parameter
    [Arguments]
    ...    @{pdo_map_values}
    ...    ${node_id}=0
    ...    ${pdo_mapping_parameter_name}=None

    BuiltIn.Log    Map the entry to PDO mapping parameters
    FOR    ${index}    ${pdo_map_value}    IN ENUMERATE    @{pdo_map_values}
        ${int_val} =   BuiltIn.Convert To Integer    item=${pdo_map_value}
        DeviceUnderTest.Write Sdo
        ...    node_id=${node_id}
        ...    index_name=${pdo_mapping_parameter_name}
        ...    sub_name=${index+1}
        ...    data=${int_val}
    END
