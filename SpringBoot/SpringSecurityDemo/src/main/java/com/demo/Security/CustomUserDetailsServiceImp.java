package com.demo.Security;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.demo.Entity.User;
import com.demo.Repository.UserRepository;

@Service
public class CustomUserDetailsServiceImp implements UserDetailsService {

	@Autowired
	private UserRepository userRepo;
	
	@Override
	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
	User user=	this.userRepo.findByEmail(username).orElseThrow(()->new RuntimeException("user not found in this email"));
	
	List<GrantedAuthority> authority=new ArrayList<>();
	return new org.springframework.security.core.userdetails.User(user.getEmail(),user.getPassword(),authority);
	}

}
