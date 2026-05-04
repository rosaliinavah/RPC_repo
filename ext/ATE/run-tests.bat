ECHO OFF
rem Execute tests from tests folder, except smoke test using test tag
python -m robot ^
--pythonpath python_libs ^
--pythonpath robot ^
--pythonpath robot/resources ^
--variable PLC_DEVICE_NAME:%computername% ^
--outputdir results ^
--exclude smokeORbroken ^
robot/tests
