ECHO OFF
rem Use 'rem' to comment out commands that are not needed

rem Dry Run System tests
rem python -m robot --pythonpath ext/ATE/python_libs --dryrun --pythonpath ./robot --outputdir results -L TRACE:INFO --include * --exclude broken robot/tests_system

rem Dry Run Integration tests
python -m robot --pythonpath ext/ATE/python_libs --dryrun --pythonpath ./robot --outputdir results -L TRACE:INFO --include * --exclude broken robot/tests_integration/20_pi_1ch_all_measurements.robot


rem Dry Robot framework linter
rem python ./ext/ATE/run_rflint.py ./robot

python ./ext/ATE/run_rflint.py robot\tests_integration\20_pi_1ch_all_measurements.robot