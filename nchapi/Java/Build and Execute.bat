javac NCHAPIClient.java
md nch
md nch\api
move NCHAPIClient.class nch\api
javac CLIClient.java
move CLIClient.class nch\api
javac GUIClient.java
move GUIClient*.class nch\api
cls
@echo off
echo Running CLI Client...
java nch.api.CLIClient
echo.
echo Running GUI Client...
java nch.api.GUIClient
