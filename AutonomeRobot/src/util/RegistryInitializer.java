package util;

import javax.servlet.ServletContext;


public class RegistryInitializer {
	
private static boolean initialized;
	
	static{
		initialized = false;
	}
	
	public static void initialize(ServletContext context){
		initialized = true;
	}
	
	public static boolean initialized(){
		return initialized;
	}
}
