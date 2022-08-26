package nch.api;

import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Toolkit;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.UIManager;

public class GUIClient
extends JFrame 
implements ActionListener {

   public GUIClient() {
      super();
      try {
         UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
      }
      catch(Exception e) {
         System.out.println("Error setting native LAF: " + e);
      }

      setTitle("Java JNI Test Client");
      setSize(250, 150);

      JButton button = new JButton("Send Command");
      button.setMinimumSize(new Dimension((int)(button.getWidth() * 1.5), button.getHeight() * 2));

      button.addActionListener(this);
      getContentPane().add("Center", button);
      show();

      addWindowListener(new WindowAdapter() { 
         public void windowClosing(WindowEvent event) {
            System.exit(0);
         }
      } );
      centerWindow(250, 150);
   }

   public void actionPerformed(ActionEvent event) {
      String serverKey = "APITestServer";
      String[] szArgs = {
         "-showmessagebox",
         "This is the test message which should be shown\nat the message box window.",
         "Test message box caption." 
      };

      NCHAPIClient client = new NCHAPIClient();
      if (client.sendCommand(serverKey, szArgs) == NCHAPIClient.NCHAPI_SUCCESS) {
         JOptionPane.showMessageDialog(null, client.getResultString(), "Result", JOptionPane.INFORMATION_MESSAGE);
      }
      else {
         JOptionPane.showMessageDialog(null, "Error: " + client.getResultString(), "Result", JOptionPane.INFORMATION_MESSAGE);
      }
   }

   public void centerWindow(int windowWidth, int windowHeight) {
      Dimension d = Toolkit.getDefaultToolkit().getScreenSize();
      this.setBounds((d.width - windowWidth)/2, (d.height - windowHeight)/2, windowWidth, windowHeight);
   }


   public static void main(String args[]) {
      new GUIClient();
   }
}

