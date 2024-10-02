package com.demo.security;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.demo.entity.User;
import com.demo.repository.UserRepository;

@Service
public class CustomUserDetailsServiceImp implements UserDetailsService{
@Autowired
private UserRepository userRepo;
	
	@Override
	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
User user = this.userRepo.findByEmail(username).orElseThrow(()->new RuntimeException("user not found"));
		
		return user;
	}

}
