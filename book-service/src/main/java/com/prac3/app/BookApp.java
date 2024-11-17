package com.prac3.app;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
//
//import com.google.auth.oauth2.GoogleCredentials;
//import com.google.firebase.FirebaseApp;
//import com.google.firebase.FirebaseOptions;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.servers.Server; 
 

@OpenAPIDefinition(servers = {@Server(url = "/", description = "Default Server URL")})
@SpringBootApplication 
@EnableDiscoveryClient
public class BookApp 
{
    public static void main( String[] args ) throws IOException
    {
//    	FileInputStream serviceAccount;
//		try {
//			serviceAccount = new FileInputStream("C:\\Users\\Shruti\\eclipse-workspace\\app\\src\\main\\resources\\my-first-project-e8d1a-firebase-adminsdk-1bes9-9a77c3f9f2.json");
//			FirebaseOptions options = FirebaseOptions.builder()
//					.setCredentials(GoogleCredentials.fromStream(serviceAccount))
//					.build();
//			
//	        if (FirebaseApp.getApps().isEmpty()) {
//	            FirebaseApp.initializeApp(options);
//	        }
//		} catch (Exception e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}

    	SpringApplication.run(BookApp.class, args);	
    }
}
