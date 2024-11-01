package com.demo.security;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
@EnableWebSecurity
public class MyConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http.csrf(csrf->csrf.disable())
		.authorizeHttpRequests(auth->auth.anyRequest().authenticated())
//		.formLogin(Customizer.withDefaults());
//		.formLogin(form->form.defaultSuccessUrl("/success")); //after login redirect auto
		.oauth2Login(oAuth->oAuth.defaultSuccessUrl("http://localhost:5173/dashboard",true)); // after login in github then redirect in /success page
		return http.build();
	}
	
//	@Bean
//	public WebMvcConfigurer corsConfigure() {
//		return new WebMvcConfigurer() {
//			@Override
//			public void addCorsMappings(CorsRegistry registry) {
//				registry.addMapping("/**")
//				.allowedOrigins("http://localhost:5173")
//				.allowedMethods("GET","POST","PUT","DELETE","OPTIONS")
//				.allowedHeaders("*")
//				.allowCredentials(true);
//			}
//		};
//	}
}
