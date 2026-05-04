REM Create python virtual environment
python -m venv virtual_env

REM Active python virtual environment
call virtual_env\Scripts\activate.bat

REM update PIP
python -m pip install --upgrade pip

REM Install PIP packages
pip install -r requirements.txt