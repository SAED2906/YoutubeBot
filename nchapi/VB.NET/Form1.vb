Public Class MainForm
    Private Sub buttonSendCommand_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles buttonSendCommand.Click
        Dim comClient As New NCHApi.Client()
        
        Dim ServerKey As String = "APITestServer"
        Dim nArgs As Integer = 3
        Dim szArgs As String() = New String() _
         {"-showmessagebox", _
          "This is the test message which should be shown" & Chr(13) & Chr(10) & "at the message box window.", _
          "Test message box caption."}
        Dim szResultString As String = ""

        Dim res As NCHApi.NCHAPIResult
        res = comClient.SendCommand(ServerKey, nArgs, szArgs, szResultString)
        If (res = NCHApi.NCHAPIResult.Success) Then
            MsgBox(szResultString, MsgBoxStyle.OkOnly & MsgBoxStyle.Information, "Result")
        Else
            MsgBox(szResultString, MsgBoxStyle.OkOnly & MsgBoxStyle.Critical, "Result")
        End If
    End Sub
End Class
