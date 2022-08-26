@echo off
echo Result
nchapi.exe APITestServer -showmessagebox "This is the test message which should be shown at the message box window." "Test message box caption."
echo.
pause
