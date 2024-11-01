package com.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Auth {
@GetMapping("/success")
public String success() {
	return "this is success page";
}
}
