<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class MainForm
   Inherits System.Windows.Forms.Form

   'Form overrides dispose to clean up the component list.
   <System.Diagnostics.DebuggerNonUserCode()> _
   Protected Overrides Sub Dispose(ByVal disposing As Boolean)
      If disposing AndAlso components IsNot Nothing Then
         components.Dispose()
      End If
      MyBase.Dispose(disposing)
   End Sub

   'Required by the Windows Form Designer
   Private components As System.ComponentModel.IContainer

   'NOTE: The following procedure is required by the Windows Form Designer
   'It can be modified using the Windows Form Designer.  
   'Do not modify it using the code editor.
   <System.Diagnostics.DebuggerStepThrough()> _
   Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(MainForm))
        Me.buttonSendCommand = New System.Windows.Forms.Button
        Me.SuspendLayout()
        '
        'buttonSendCommand
        '
        Me.buttonSendCommand.Location = New System.Drawing.Point(45, 30)
        Me.buttonSendCommand.Name = "buttonSendCommand"
        Me.buttonSendCommand.Size = New System.Drawing.Size(150, 50)
        Me.buttonSendCommand.TabIndex = 0
        Me.buttonSendCommand.Text = "Send Command"
        Me.buttonSendCommand.UseVisualStyleBackColor = True
        '
        'MainForm
        '
        Me.AcceptButton = Me.buttonSendCommand
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(242, 116)
        Me.Controls.Add(Me.buttonSendCommand)
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.MaximizeBox = False
        Me.MaximumSize = New System.Drawing.Size(250, 150)
        Me.MinimumSize = New System.Drawing.Size(250, 150)
        Me.Name = "MainForm"
        Me.Text = "VB.NET Test Client"
        Me.ResumeLayout(False)

    End Sub
   Friend WithEvents buttonSendCommand As System.Windows.Forms.Button

End Class
