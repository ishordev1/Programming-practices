package com.aiIntigration.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.aiIntigration.serviceImpl.GeminiChatService;

@RestController
@CrossOrigin("http://localhost:5173")
public class GeminiController {
	@Autowired
	private GeminiChatService geminiService;
	
	@PostMapping("/chat")
	public ResponseEntity<String> chat(@RequestBody String prompt){
		
	String chat = this.geminiService.chat(prompt);
	return new ResponseEntity<String>(chat,HttpStatus.OK);
}
}
