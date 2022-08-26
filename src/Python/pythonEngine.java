package Python;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class pythonEngine {
	
	public static void main(String[]args) throws Exception {
		Python_Download("https://www.youtube.com/watch?v=mKQ9uXIjulc");
	}

	public static void Python_Download(String Path) throws Exception {
	    ProcessBuilder processBuilder = new ProcessBuilder("python", "main.py", Path);
	    processBuilder.redirectErrorStream(true);
	    Process process = processBuilder.start();
	    
	    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
	    
		StringBuilder builder = new StringBuilder();
		String line = null;
		while ( (line = reader.readLine()) != null) {
			builder.append(line);
			builder.append(System.getProperty("line.separator"));
		}
		
		String result = builder.toString();
	    System.out.println(result);
	}
	
}
