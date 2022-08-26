package nch.api;

import java.io.File;

/**
This is a class for interacting with the NCH API.  While it is possible to make a call directly to the nchapi.dll, it is recommended that developers use this interface, instead.  If developers wish to call the nchapi.dll without the use of this particular class, they will need to declare a class that contains at least the following:
<code>
   package nch.api;

   public class NCHAPIClient {
      private static native int NCHAPISendCommand(String szServerKey, int nArgs, String[] szArgs, String[] szResultString);
   }
</code><p>
Developers will also need to load the nchapi.dll library themselves (by means of either <code>System.load(...);</code> or <code>System.loadLibrary(...)</code>.
<p>
<b>Using this class</b>
In order to use this class to call the NCH API, declare an instance of this class and then call the <code>sendCommand()</code> method, passing in the name of the application to call and the arguments of the API call.<p> The return value of the <code>sendCommand()</code> method will give an overall indication of whether the call was successful or not (see <code>NCHAPI_*</code>), and more verbose information about the call's status can be retrieved by means of the <code>getResultString()</code> method.  For example:<p>
<code>
   String appName = "APITestServer";
   String[] args = new String[3];
   testArgs[0] = "-showmessagebox";
   testArgs[1] = "This is the test message which should be shown \n at the message box window.";
   testArgs[2] = "Test message box caption.";

   NCHAPIClient client = new NCHAPIClient();
   int result = client.sendCommand(appName, arguments);
   String resultString = client.getResultString();
</code>
*/
public class NCHAPIClient {

/**
A return code indicating that the API call was successful.
*/
public static final int NCHAPI_SUCCESS = 0;

/**
A return code indicating that the API call encountered an error and was 
not successful.
*/

public static final int NCHAPI_ERROR = -1;

/**
A return code indicating that the API call could not be completed because the application for which the API call was destined was not running.
*/
public static final int NCHAPI_CODE_NOTFOUND = -2;

/**
The native method residing in the dll that will be called.
@param szServerKey the name of the program to which the API call should be routed.  This must not be null.
@param nArgs the number of arguments being passed in.
@param szArgs the arguments to the program.  This array, and all of its elements, must not be null.
@param szResultString the array into which the verbose result string will be placed.  This array needs to be declared prior to the native call.  It must be a 1-element array, such as:<br>
<code>
   String[] szResultString = new String[1];
</code>
@return an integer that indicates the success or failure of the call.  See NCHAPI_*.
*/
private static native int NCHAPISendCommand(String szServerKey, int nArgs, String[] szArgs, String[] szResultString);

private String szServerKey = null;
private String[] szArgs = null;
private String[] szReturnString = null;

/**
Constructor.  This loads the static library via <code>System.loadLibrary("nchapi");</code>.  This means that the JVM will look through the directories in the PATH (in the order they are found) for <code>nchapi.dll</code>, and will load the first one that is found.
@throws SecurityException if a security manager exists and its checkLink method doesn't allow loading of the specified dynamic library.
@throws UnsatisfiedLinkError if the library could not be found.
*/
public NCHAPIClient() 
throws SecurityException, UnsatisfiedLinkError {
   System.loadLibrary("nchapi");
}

/**
Constructor.  This loads the static library via <code>System.load(pathToDll);</code>.  This means that the JVM will try to load the <code>nchapi.dll</code> found in the passed-in path.
@param pathToDLL the full path to where the DLL should be loaded from.
@throws SecurityException if a security manager exists and its checkLink method doesn't allow loading of the specified dynamic library.
@throws UnsatisfiedLinkError if the library could not be found.
*/
public NCHAPIClient(String pathToDLL) 
throws SecurityException, UnsatisfiedLinkError {
    System.load(pathToDLL + File.separator + "nchapi.dll");
}

/**
Cleans up member variables.
@throws Throwable if an error occurs during finalization.
*/
public void finalize()
throws Throwable {
   if (szServerKey != null) {
      szServerKey = null;
   }

   if (szArgs != null) {
      for (int i = 0; i < szArgs.length; i++) {
         szArgs[i] = null;
      }
      szArgs = null;
   }

   if (szReturnString != null) {
      szReturnString[0] = null;
      szReturnString = null;
   }
   super.finalize();
}

/**
Returns the verbose result string indicating what happened during the API call.
@return a String describing in more detail than NCHAPI_* what occurred during the API call.
*/
public String getResultString() {
   return szReturnString[0];
}

/**
Sends the command defined by the program key and arguments to <code>nchapi.dll</code>.
@param serverKey the program to which the API call should be directed.  This must not be null.
@param args the arguments to pass to the program API call.  This array, and all of its elements, must not be null.
@return an integer value that gives a general indication of what happened in the API call.  See <code>NCHAPI_*</code>.
@throws NullPointerException if any of the required parameters were null.
*/
public int sendCommand(String serverKey, String[] args) 
throws NullPointerException {
   setServerKey(serverKey);
   setArguments(args);
   szReturnString = new String[1];
   return NCHAPISendCommand(szServerKey, szArgs.length, szArgs, szReturnString);
}

/**
Sets the program arguments and checks them for null values.
*/
private void setArguments(String[] args) 
throws NullPointerException {
   if (args == null) {
      throw new NullPointerException("The argument array cannot be null.");
   }
   for (int i = 0; i < args.length; i++) {
      if (args[i] == null) {
         throw new NullPointerException("Argument array memeber #" + i + " cannot be null.");
      }
   }
   szArgs = args;
}

/**
Sets the program key and checks it for null values.
*/
private void setServerKey(String serverKey) 
throws NullPointerException {
   if (serverKey == null) {
      throw new NullPointerException("The program key cannot be null.");
   }
   szServerKey = serverKey;
}

}
