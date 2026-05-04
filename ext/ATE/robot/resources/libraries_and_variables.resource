*** Settings ***
Documentation       Main resource file for ATE test environment.

Library             Collections
Library             Process

Library             interfaces.codesys.codesys_client                   config_file=${CODESYS_CONFIG_FILE}
...                                                                     AS  codesys_client
Library             interfaces.codesys.codesys_rpc_client               uri=${CODESYS_RPC_SERVER}
...                                                                     timeout=${CODESYS_RPC_TIMEOUT_S}
...                                                                     AS  codesys_rpc_client
Library             devices.national_instrument.veristand               veristand_server_path=${VERISTAND_GATEWAY_PATH}
...                                                                     ip_address=${VERISTAND_IP_ADDRESS}
...                                                                     AS  veristand_api
Library             devices.national_instrument.real_time_sequences     AS  RealTimeSequences
Library             utilities.codesys.codesys_executer                  config_file=${CODESYS_CONFIG_FILE}
...                                                                     AS  codesys_executer
Library             utilities.exe_runner.exe_runner                     ${CODESYS_LOCATION}
...                                                                     --profile="${CODESYS_PROFILE}"
...                                                                     --noUI
...                                                                     --runscript="${CODESYS_RPC_SERVER_API}"
...                                                                     search_text=CODESYS READY
...                                                                     AS  codesys_rpc_executer
Library             utilities.exe_runner.exe_runner                     ${CODESYS_CONTROL_WIN_SERVICE_LOCATION}
...                                                                     -d
...                                                                     search_text=registered at the OPC UA server
...                                                                     AS  codesys_control_service_executer
Library             utilities.exe_runner.exe_runner                     ${CODESYS_ETH_GATEWAY_LOCATION}
...                                                                     -d
...                                                                     search_text=Running as network server
...                                                                     AS  CodesysEthGateway
Library             utilities.exe_runner.exe_runner                     ${CODESYS_CAN_GATEWAY_LOCATION}
...                                                                     -d
...                                                                     search_text=Running as network server
...                                                                     AS  CodesysCanGateway
Library             utilities.xnet_db_utility.xnet_db_utility           veristand_sdf_filepath=${VERISTAND_SDF_DEMO_PATH}
...                                                                     xnet_db_folder=${VERISTAND_XNET_DB_FOLDER_PATH}
...                                                                     AS  xnet_db_utility
Library             utilities.parser.alias_xml_parser                   AS  alias_xml_parser
Library             utilities.can_loader.can_loader                     can_card_serial=12345
...                                                                     device_serial_number=12345678
...                                                                     AS  CanLoader
Resource            veristand_aliases.resource


*** Variables ***
${PATH_TO_FIRMWARE_FOLDER} =                        ${EXECDIR}
${PATH_TO_APPLICATION_FOLDER} =                     ${EXECDIR}

${VERISTAND_IP_ADDRESS} =                           localhost
${VERISTAND_GATEWAY_PATH} =                         C:\\Program Files\\National Instruments\\VeriStand 2023\\veristand-server.exe
${VERISTAND_SDF_DEMO_PATH} =                        ${EXECDIR}\\veristand\\Engine Demo\\Engine Demo.nivssdf
${VERISTAND_SDF_PATH} =                             ${EXECDIR}\\veristand\\Epec Base Project\\Epec Base Project.nivssdf
${VERISTAND_XNET_DB_FOLDER_PATH} =                  ${EXECDIR}\\veristand\\Epec Base Project\\XNET DBs
${VERISTAND_ALIASES_RESOURCE_PATH} =                ${EXECDIR}\\robot\\resources\\veristand_aliases.resource
${VERISTAND_SDF_DEPLOY_TIMEOUT_S} =                 60
${VERISTAND_START_TIMEOUT_S} =                      60
${VERISTAND_STOP_TIMEOUT_S} =                       30

${CODESYS_CONFIG_FILE} =                            ${EXECDIR}\\python_libs\\interfaces\\codesys\\codesys_config.cfg
${CODESYS_SERVER_API} =                             ${EXECDIR}\\python_libs\\interfaces\\codesys\\codesys_server.py
${CODESYS_TEST_APP_PROJECT} =                        ${EXECDIR}\\codesys\\Codesys Win Test Application\\codesys-windows-test-application.project
${CODESYS_START_TIMEOUT} =                          90
${CODESYS_CONTROL_WIN_SERVICE_START_TIMEOUT} =      90
${CODESYS_DEVICE_VERSION} =                         3.5.19.0

${CODESYS_RPC_CONFIG_FILE} =                        ${EXECDIR}\\robot\\config\\codesys_rpc_config.cfg
${CODESYS_RPC_SERVER_API} =                         ${EXECDIR}\\python_libs\\interfaces\\codesys\\codesys_rpc_server.py
${CODESYS_RPC_SERVER} =                             http://127.0.0.1:8270
${CODESYS_RPC_TIMEOUT_S} =                          120s

${CODESYS_LOCATION} =                               C:\\Program Files (x86)\\CODESYS 3.5.19.0\\CODESYS\\Common\\CODESYS.exe
${CODESYS_CONTROL_WIN_SERVICE_LOCATION} =           C:\\Program Files (x86)\\CODESYS 3.5.19.0\\GatewayPLC\\CODESYSControlService.exe
${CODESYS_ETH_GATEWAY_LOCATION} =                   ${EXECDIR}\\codesys\\EthGateway\\GatewayService.exe
${CODESYS_CAN_GATEWAY_LOCATION} =                   ${EXECDIR}\\codesys\\CanGateway\\GatewayService.exe
${CODESYS_PROFILE} =                                CODESYS V3.5 SP19

${IP_ADDRESS} =                                     localhost
${PLC_DEVICE_NAME} =                                %{COMPUTERNAME}     # PC name when running on Windows
${PLC_DEVICE_IP} =                                  01D0
${PLC_USERNAME} =                                   test
${PLC_PASSWORD} =                                   test123

${CAN_BUSTYPE} =                                    kvaser
${CAN_CHANNEL} =                                    0
${CAN_BITRATE} =                                    250000

${FW_NODE_ID} =                                     127
${FW_EDS_FILE} =                                    dummy.eds
${FW_BIN_FILE} =                                    dummy.app

${APP_NODE_ID} =                                    126
${APP_EDS_FILE} =                                   dummy.eds
${APP_BIN_FILE} =                                   dummy.app

${SAFETY_PRODUCT} =                                 False
