namespace COMClientTest
{
   partial class FormMainDialog
   {
      /// <summary>
      /// Required designer variable.
      /// </summary>
      private System.ComponentModel.IContainer components = null;

      /// <summary>
      /// Clean up any resources being used.
      /// </summary>
      /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
      protected override void Dispose(bool disposing)
      {
         if (disposing && (components != null))
         {
            components.Dispose();
         }
         base.Dispose(disposing);
      }

      #region Windows Form Designer generated code

      /// <summary>
      /// Required method for Designer support - do not modify
      /// the contents of this method with the code editor.
      /// </summary>
      private void InitializeComponent()
      {
          System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormMainDialog));
          this.buttonSendCommand = new System.Windows.Forms.Button();
          this.SuspendLayout();
          // 
          // buttonSendCommand
          // 
          this.buttonSendCommand.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F);
          this.buttonSendCommand.Location = new System.Drawing.Point(45, 30);
          this.buttonSendCommand.Name = "buttonSendCommand";
          this.buttonSendCommand.Size = new System.Drawing.Size(150, 50);
          this.buttonSendCommand.TabIndex = 0;
          this.buttonSendCommand.Text = "Send Command";
          this.buttonSendCommand.UseVisualStyleBackColor = true;
          this.buttonSendCommand.Click += new System.EventHandler(this.buttonSendCommand_Click);
          // 
          // FormMainDialog
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(242, 116);
          this.Controls.Add(this.buttonSendCommand);
          this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
          this.MaximizeBox = false;
          this.MaximumSize = new System.Drawing.Size(250, 150);
          this.MinimumSize = new System.Drawing.Size(250, 150);
          this.Name = "FormMainDialog";
          this.Text = "C# .NET Test Client";
          this.ResumeLayout(false);

      }

      #endregion

      private System.Windows.Forms.Button buttonSendCommand;
   }
}

