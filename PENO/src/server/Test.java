package server;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.URL;
import java.util.Scanner;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

@SuppressWarnings("restriction")
public class Test {

	public static void main(String[] args) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(54322), 0);
        server.createContext("/test", new MyHandler());
        server.createContext("/up", new UpHandler());
        server.setExecutor(null); // creates a default executor
        server.start();
    }

    static class MyHandler implements HttpHandler {
        public void handle(HttpExchange t) throws IOException {
        	URL url = Test.class.getClassLoader().getResource("server/test.txt");
        	InputStream stream = url.openStream();
        	Scanner scanner = new Scanner(stream);
    		Scanner scanner2 = scanner.useDelimiter("\\A");
    		String response = "";
    		while(scanner.hasNext()){
    			response = response + scanner.next();
    		}
    		scanner.close();
    		scanner2.close();
        	
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
    
    
    
    static class UpHandler implements HttpHandler {
        public void handle(HttpExchange t) throws IOException {
            String response = "Going up!";
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}