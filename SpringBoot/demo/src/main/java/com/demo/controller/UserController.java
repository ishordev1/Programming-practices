package com.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.demo.entity.User;
import com.demo.jwt.JwtHelper;
import com.demo.repository.UserRepository;
import com.demo.security.Request;
import com.demo.security.Response;

@RestController
public class UserController {
	@Autowired
	private PasswordEncoder passwordEncorder;
	 @Autowired
	 private AuthenticationManager authManager;
	

	    @Autowired
	    private JwtHelper helper;

	    @Autowired
	    private UserDetailsService userDetailsService;
	    
	@Autowired
	private UserRepository userRepo;
	
	
	@GetMapping("/test")
public ResponseEntity<String> test(){
	return ResponseEntity.ok("this is testing text");
}

	@PostMapping("/signup")
public ResponseEntity<User> signup(@RequestBody User user){
		user.setPassword(this.passwordEncorder.encode(user.getPassword()));
		User save = this.userRepo.save(user);
	return new ResponseEntity<>(save,HttpStatus.CREATED);
}
	
	@PostMapping("/signin")
public ResponseEntity<Response> signin(@RequestBody Request request){
		Authentication authenticate = this.authManager.authenticate(new UsernamePasswordAuthenticationToken(request.getEmail(), request.getPassword()));
        UserDetails userDetails = userDetailsService.loadUserByUsername(request.getEmail());
        User user=(User) userDetails;
        String token = this.helper.generateToken(userDetails);
		Response res=Response.builder().token(token).user(user).build();
		return new ResponseEntity<>(res,HttpStatus.CREATED);
}
	
}
