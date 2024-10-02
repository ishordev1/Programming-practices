package com.demo.security;

import org.springframework.security.core.userdetails.UserDetails;

import com.demo.entity.User;

import lombok.Builder;
import lombok.Data;
@Data
@Builder
public class Response {
private String token;
private User user;
}
