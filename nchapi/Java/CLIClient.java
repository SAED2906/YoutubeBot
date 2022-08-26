package nch.api;

/**
This class is provided merely as an example of how to call and use the provided NCHAPIClient class.
*/
public class CLIClient {

public static void main(String[] args) {
   String serverKey = null;
   String[] szArgs = new String[3];

   serverKey = "APITestServer";
   szArgs[0] = "-showmessagebox";
   szArgs[1] = "This is the test message which should be shown\nat the message box window.";
   szArgs[2] = "Test message box caption.";

   NCHAPIClient client = new NCHAPIClient();
   int result = client.sendCommand(serverKey, szArgs);
   if (result == client.NCHAPI_SUCCESS) {
      System.out.println("Result (" + result + "): " + client.getResultString());
   }
   else if (result == client.NCHAPI_ERROR) {
      System.out.println("Error (" + result + "): " + client.getResultString());
   }
   else if (result == client.NCHAPI_CODE_NOTFOUND) {
      System.out.println("Error (" + result + "): " + client.getResultString());
   }
}

}
