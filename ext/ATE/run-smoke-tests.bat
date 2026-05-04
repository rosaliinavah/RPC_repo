ECHO OFF
rem Execute tests from test folder using smoke tag
python -m robot ^
--pythonpath python_libs ^
--pythonpath robot ^
--pythonpath robot/resources ^
--variable PLC_DEVICE_NAME:%computername% ^
--outputdir results ^
--include smoke ^
--exclude broken ^
robot/smoke
