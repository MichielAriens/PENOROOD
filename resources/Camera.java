package cwRobot;

import java.awt.image.BufferedImage;
import java.io.*;
import java.net.MalformedURLException;

import javax.imageio.*;
import javax.swing.*;

import com.google.zxing.BinaryBitmap;
import com.google.zxing.LuminanceSource;
import com.google.zxing.MultiFormatReader;
import com.google.zxing.ReaderException;
import com.google.zxing.Result;
import com.google.zxing.client.j2se.*;
import com.google.zxing.common.HybridBinarizer;

public class Camera {
 //werkt, kan file aanmaken emptyfile in derp/cw/...
       public static void main(String args[]) {
    	   int test = 2;
    	   if(test == 2){
            execute_command();
    	   }
    	   else{
    		   String decodedInstruction = readQRcode("C:\\Users\\simon\\qrtest.jpg");
    		   System.out.println(decodedInstruction);
    	   }
        }

	private static void execute_command() {
		try {
		    Runtime rt = Runtime.getRuntime();
		    //Process pr = rt.exec("cmd /c echo. 2>EmptyFile.txt");
		    Process pr = rt.exec("raspistill -o pics/image.jpg");
		    //Process pr = rt.exec("c:\\helloworld.exe");
 
		    BufferedReader input = new BufferedReader(new InputStreamReader(pr.getInputStream()));
 
		    String line=null;
 
		    while((line=input.readLine()) != null) {
		        System.out.println(line);
		    }
 
		    int exitVal = pr.waitFor();
		    System.out.println("Exited with error code "+exitVal);
 
		} catch(Exception e) {
		    System.out.println(e.toString());
		    e.printStackTrace();
		}
	}
       
       public static String readQRcode(String pathname){
    	   
    	File file = new File(pathname);
    	
    	try {
			Icon imageIcon = new ImageIcon(file.toURI().toURL());
		} catch (MalformedURLException e) {
			e.printStackTrace();
			System.out.println("fout bij converteren van file naar image");
		}
    	String decodeText = getDecodeText(file);
    	//System.out.println(decodeText);
    	return decodeText;
       }

	private static String getDecodeText(File file) {
		BufferedImage image;
	    try {
	      image = ImageIO.read(file);
	    } catch (IOException ioe) {
	      return ioe.toString();
	    }
	    if (image == null) {
	      return "Could not decode image";
	    }
	    LuminanceSource source = new BufferedImageLuminanceSource(image);
	    BinaryBitmap bitmap = new BinaryBitmap(new HybridBinarizer(source));
	    Result result; 
	    try { result = new MultiFormatReader().decode(bitmap);
	    } catch (ReaderException re) {
	      return re.toString();
	    }
	    return result.getText();
	  }
}