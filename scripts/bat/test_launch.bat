@echo off

SET PYLAUNCHER_PATH=%~dp0..\..\dist\pylauncher.exe
SET TEST_PATH=%~dp0..\..\tests\test_launch.py

%PYLAUNCHER_PATH% %TEST_PATH%
