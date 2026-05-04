*** Settings ***
Documentation       Main resource file for ATE test environment.

Library             OperatingSystem
Library             String
Library             Collections

#Library             devices.national_instrument.veristand       veristand_server_path=${VERISTAND_GATEWAY_PATH}
#...                                                             ip_address=${VERISTAND_IP_ADDRESS}
#...                                                             AS  VeristandApi
Library             interfaces.codesys.codesys_rpc_client       uri=${CODESYS_RPC_SERVER}      timeout=${CODESYS_RPC_TIMEOUT_S}
...                                                             AS  CodesysRpcClient
Library             utilities.exe_runner.exe_runner             ${CODESYS_LOCATION}
...                                                             --profile="${CODESYS_PROFILE}"
...                                                             --noUI
...                                                             --runscript="${CODESYS_RPC_SERVER_API}"
...                                                             search_text=CODESYS READY
...                                                             AS  CodesysRpcExecuter
Library             utilities.exe_runner.exe_runner             ${CODESYS_CAN_GATEWAY_LOCATION}
...                                                             -d
...                                                             search_text=Running as network server
...                                                             AS  CodesysCanGateway
#Library             utilities.xnet_db_utility.xnet_db_utility   veristand_sdf_filepath=${VERISTAND_SDF_PATH_SYSTEM}
#...                                                             xnet_db_folder=${VERISTAND_XNET_DB_FOLDER_PATH}
#...                                                             AS  XnetDbUtility
Library             devices.epec.epec_canopen                   bustype=${CAN1_BUSTYPE}
...                                                             channel=${CAN1_CHANNEL}
...                                                             bitrate=${CAN1_BITRATE}
...                                                             AS  DeviceUnderTest_CAN1
#Library             devices.epec.epec_canopen                   bustype=${CAN3_BUSTYPE}
#...                                                             channel=${CAN3_CHANNEL}
#...                                                             bitrate=${CAN3_BITRATE}
#...                                                             AS  DeviceUnderTest_CAN3
Library             utilities.bit_operations.bit_operations     AS  BitOperations
Library             utilities.parser.alias_xml_parser           AS  AliasXmlParser

Resource            resources/veristand_aliases.resource
Resource            resources/veristand_xnet_db.resource


*** Variables ***
${VERISTAND_IP_ADDRESS} =                           localhost
${VERISTAND_GATEWAY_PATH} =                         C:\\Program Files\\National Instruments\\VeriStand 2023\\veristand-server.exe
${VERISTAND_PATH} =                                 ${EXECDIR}\\veristand\\SC4X1-01-Project
${VERISTAND_SDF_PATH_SYSTEM} =                      ${VERISTAND_PATH}\\SC4X1-01-System.nivssdf
${VERISTAND_INTEGRATION_1_SDF_PATH} =               ${VERISTAND_PATH}\\SC4X1-01-Integration-1.nivssdf
${VERISTAND_INTEGRATION_2_SDF_PATH} =               ${VERISTAND_PATH}\\SC4X1-01-Integration-2.nivssdf

${VERISTAND_SYSTEM_ALIASES_RESOURCE_PATH} =         ${EXECDIR}\\robot\\resources\\veristand_aliases.resource
${VERISTAND_INTEGRATION_1_ALIASES_RESOURCE_PATH} =  ${EXECDIR}\\robot\\resources\\veristand_aliases.resource
${VERISTAND_INTEGRATION_2_ALIASES_RESOURCE_PATH} =  ${EXECDIR}\\robot\\resources\\veristand_aliases.resource

${VERISTAND_XNET_DB_FOLDER_PATH} =                  ${VERISTAND_PATH}\\XNET DBs
${VERISTAND_SDF_DEPLOY_TIMEOUT_S} =                 120
${VERISTAND_START_TIMEOUT_S} =                      60
${VERISTAND_STOP_TIMEOUT_S} =                       30

${CODESYS_RPC_SERVER_API} =                         ${EXECDIR}\\ext\\ATE\\python_libs\\interfaces\\codesys\\codesys_rpc_server.py
${CODESYS_RPC_SERVER} =                             http://127.0.0.1:8270
${CODESYS_RPC_TIMEOUT_S} =                          120
${CODESYS_RPC_SLEEP_BEFORE_READ_S} =                0.25s  # CODESYS Default device monitoring interval is 200ms

#${CODESYS_SYSTEM_TEST_APP_PROJECT} =                ${EXECDIR}\\apps\\MTC_SC4X1_01\\SC4X1_01_System\\SC4X1_01_System.project
#${CODESYS_INTEGRATION_TEST_APP_PROJECT_1} =         ${EXECDIR}\\apps\\integration_test_applications\\SC4X1_01_Integration.project
${CODESYS_TEST_PROJECT} =                           ${EXECDIR}\\apps\\CodesysRPC\\RAU\\RAU.project

${CODESYS_LOCATION} =                               C:\\Program Files (x86)\\CODESYS 3.5.19.60\\CODESYS\\Common\\CODESYS.exe

${CODESYS_CAN_GATEWAY_LOCATION} =                   ${EXECDIR}\\ext\\ATE\\codesys\\CanGateway\\GatewayService.exe
${CODESYS_ETH_GATEWAY_LOCATION} =                   ${EXECDIR}\\robot\\codesys\\EthGateway\\GatewayService.exe
${CODESYS_PROFILE} =                                CODESYS V3.5 SP19 Patch 6
${CODESYS_GATEWAY_EXECUTION_START_TIMEOUT} =        30

${PATH_TO_FIRMWARE_FOLDER} =                        ${EXECDIR}\\artifacts\\firmware

${PATH_TO_APPLICATION_FOLDER} =                     ${EXECDIR}\\apps


${PATH_TO_FW_METADATA} =                            ${OUTPUT_DIR}\\fw_metadata.txt
${PATH_TO_APP_METADATA} =                           ${OUTPUT_DIR}\\app_metadata.txt

${TESTCASE_INDEX} =                                 ${0}
${SLSC_LOOP_RATE_SLEEP} =                           500ms

# CAN channel 1 is for CodesysCanGateway
${CAN1_BUSTYPE} =                                   kvaser
${CAN1_CHANNEL} =                                   0
${CAN1_BITRATE} =                                   250000


${PLC_DEVICE_NAME} =                                6000-series
${PLC_SERIAL_NUMBER} =                              40154146
${PLC_DEVICE_TYPE} =                                405
${PLC_VENDOR_ID} =                                  48
${PLC_PRODUCT_CODE} =                               6200
${PLC_HW_REVISION} =                                ${PLC_PRODUCT_CODE}-C27
${PLC_REVISION_NUMBER} =                            0x18380147  # 6200 + C27 (B+01 -> 201dec -> 00C9hex)
${PLC_USERNAME} =                                   User
${PASSWORD} =                                       4146
${CODESYS_DEVICE_NAME} =                            ${PLC_DEVICE_NAME}_${PLC_SERIAL_NUMBER}
${MANUFACTURER_DEVICE_NAME} =                       SC4X1 control unit

${SAFETY_PRODUCT} =                                 True

${FW_NODE_ID} =                                     2
${APP_NODE_ID} =                                    127
${CAN3_APP_NODE_ID} =                               127

${DEFAULT_SUPPLY_VOLTAGE} =                         12

${PUK_CODE} =                                       4146
