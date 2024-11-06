package com.demo.ServiceImp;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import com.demo.Entity.User;
import com.demo.Repository.UserRepository;

@Service
public class UserServiceImp {
@Autowired
private UserRepository userRepository;

@Autowired
private  PasswordEncoder passwordEncorder;

public User createUser(User user) {
	
	user.setPassword(this.passwordEncorder.encode(user.getPassword()));
	return this.userRepository.save(user);
}

public User getUserByEmail(String email) {
return	this.userRepository.findByEmail(email).orElseThrow(()->new RuntimeException("user not found in this email"));
}

}
