using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace COMClientTest
{
   public partial class FormMainDialog : Form
   {
      NCHApi.Client apiCOMClient;
      public FormMainDialog()
      {
         InitializeComponent();
         apiCOMClient = new NCHApi.Client();
      }

      private void buttonSendCommand_Click(object sender, EventArgs e)
      {
         string ServerKey = "APITestServer";
         int nArgs = 3;
         string[] szArgs = {"-showmessagebox",
         ("This is the test message which should be shown" + Environment.NewLine + "at the message box window."),
         "Test message box caption."};
         string szResultString = "";

         if (NCHApi.NCHAPIResult.Success == apiCOMClient.SendCommand(ServerKey, nArgs, szArgs, ref szResultString))
         {
            MessageBox.Show(szResultString, "Result", MessageBoxButtons.OK, MessageBoxIcon.Information);
         }
         else
         {
            MessageBox.Show(szResultString, "Result", MessageBoxButtons.OK, MessageBoxIcon.Error);
         }
      }
   }
}