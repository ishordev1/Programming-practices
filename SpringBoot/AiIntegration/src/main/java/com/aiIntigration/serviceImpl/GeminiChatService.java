package com.aiIntigration.serviceImpl;

import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class GeminiChatService {
	//api key->	
	//url -> https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=api key
	
public String chat(String prompt) {
	final String API_KEY="APIKEY HERE";
	final String URL="https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=";
	
	HttpHeaders header=new HttpHeaders();
	header.setContentType(MediaType.APPLICATION_JSON);
	String requestBody=new JSONObject()
			.put("contents", new JSONArray()
					.put(new JSONObject()
							.put("parts",new JSONObject()
									.put("text", prompt)
									)
							)).toString();
	HttpEntity<String> requestEntity=new HttpEntity<>(requestBody,header);
	RestTemplate restTemplate=new RestTemplate();
	ResponseEntity<String> response=restTemplate.postForEntity(URL+API_KEY, requestEntity, String.class);
	return response.getBody();
	
}
}
