Dim shell, client, result
set shell = CreateObject("WScript.Shell")

' Create NCHAPIClient
set client = CreateObject("NCHAPI.Client")

' NCH Program Key
Dim ServerKey
ServerKey = "APITestServer"

Dim nArgs
nArgs = 3

Dim szArgs
szArgs = Array("-showmessagebox", "This is the test message which should be shown" & vbCrLf & "at the message box window.", "Test message box caption.")

Dim szResultString
if client.SendCommand(ServerKey, CInt(nArgs), szArgs, szResultString) = 0 then
    result = shell.Popup(szResultString, 0, "Result", 0 + 48)
else
    result = shell.Popup("Error: " + szResultString, 0, "Result", 0 + 48)
end if

' Clean up
set shell = nothing
set client = nothing
set result = nothing
