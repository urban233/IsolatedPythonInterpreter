@echo off
echo The directory of the script is:%~dp0

REM Set the path to your virtual environment
SET VENV_PATH=%~dp0..\..\.venv
SET SRC_PATH=%~dp0..\..\src\pylauncher.py

REM Ensure the virtual environment exists at the given path
IF NOT EXIST "%VENV_PATH%\Scripts\activate.bat" (
    echo Error: Virtual environment not found at "%VENV_PATH%\Scripts\activate.bat".
    exit /b
)

REM Activate the virtual environment
CALL "%VENV_PATH%\Scripts\activate.bat"

REM Run the Python command (replace this with your desired command)
pyinstaller --onefile %SRC_PATH%

REM Deactivate the virtual environment (this line is optional)
CALL deactivate