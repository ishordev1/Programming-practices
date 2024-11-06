package com.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.demo.Entity.User;
import com.demo.Security.Request;
import com.demo.ServiceImp.UserServiceImp;

@RestController
public class AuthController {

	@Autowired
private	UserServiceImp userServiceImp;
	
	@Autowired
	private AuthenticationManager authenticationManager;
	
	
	@PostMapping("/signup")
ResponseEntity<User> signup(@RequestBody User user){
	User dbUser=	this.userServiceImp.createUser(user);
		return new ResponseEntity<>(dbUser,HttpStatus.OK);
	}
	
	
	
	
	@PostMapping("/login")
	public ResponseEntity<String> login(@RequestBody Request request){
		Authentication authenticate = this.authenticationManager
		.authenticate(new UsernamePasswordAuthenticationToken(request.getEmail(), request.getPassword()));
	
	return ResponseEntity.ok(authenticate.getName());
	}
	
	
	
	

}
