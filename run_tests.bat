ECHO OFF
rem Use 'rem' to comment out commands that are not needed

rem #### SYSTEM TEST COMMANDS ####

rem Firmware download test for System Firmware
rem python -m robot --pythonpath ext/ATE/python_libs --pythonpath ./robot --outputdir results -L TRACE:INFO --include firmware_update robot/tests_system

rem Application download test for System Application
rem python -m robot --pythonpath ext/ATE/python_libs --pythonpath ./robot --outputdir results -L TRACE:INFO --include application_update robot/tests_system

rem Run Integration tests which have 'design' tag
rem python -m robot --pythonpath ext/ATE/python_libs --pythonpath ./robot --outputdir results -L TRACE:INFO --include design --exclude brokenANDfirmware_updateANDapplication_update robot/tests_system

rem Run System tests which have 'debug' tag
python -m robot --pythonpath ext/ATE/python_libs --pythonpath ./robot --outputdir results -L TRACE:INFO --include debug robot/tests_system

rem Dry Run System tests
rem python -m robot --dryrun --pythonpath ext/ATE/python_libs --pythonpath ./robot --outputdir results -L TRACE:INFO robot/tests_system

rem #### INTEGRATION TEST COMMANDS ####

rem Firmware download test for Integration Firmware
rem python -m robot --pythonpath ext/ATE/python_libs --pythonpath ./robot --outputdir results -L TRACE:INFO --include firmware_update robot/tests_integration

rem Run Integration tests which have 'design' tag
rem python -m robot --pythonpath ext/ATE/python_libs --pythonpath ./robot --outputdir results -L TRACE:INFO --include design --exclude brokenANDfirmware_updateANDapplication_update robot/tests_integration
