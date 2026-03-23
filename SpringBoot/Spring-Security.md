# Spring Security Notes
## Spring Security Follow
#login senario
#request come-> controller-> securityFilterChain -> if url public -> usernamepasswordAuthenticationtoken object create-> pass into authenticationManager -> authenticationmanager use authenticationProvider internally (not need to create object new version manager auto handle)  -> authenticationProvider use UserDetailsService interface which we implement with customuserDetailsService (loaduserbyusername method) in AuthenticationProvider has DaoAuthenticationProvider method which take original user data which come from loadUserByUsername and form data DaoAuthenticationProvider compare internally and return authenticate data.


## 1. UserDetails Implementation

- If your `User` class **implements `UserDetails`**, then you must override all methods of the `UserDetails` interface inside the `User` class.

- If your `User` class does **NOT implement `UserDetails`**, then you manually handle everything inside `CustomUserDetailsService`.

---

## 2. CustomUserDetailsService

- Implement `UserDetailsService`
- Override `loadUserByUsername()`
- Use `UserRepository` to fetch user from database
- Create method in repo: `findByEmail()`

---

### Example (Without Implementing UserDetails in User Class)

```java
@Service
public class CustomUserDetailsService implements UserDetailsService {

    @Autowired
    UserRepository userRepo;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

        User user = this.userRepo.findByEmail(username);

        if (user == null) {
            throw new ResourceNotFound("user not found");
        }

        List<GrantedAuthority> authorities = new ArrayList<>();
        authorities.add(new SimpleGrantedAuthority("ROLE_" + user.getRole()));

        return new org.springframework.security.core.userdetails.User(
                user.getEmail(),
                user.getPassword(),
                authorities
        );
    }
} 
```
## Without Role
public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

    User dbUser = userRepo.findByEmail(username)
            .orElseThrow(() -> new ResourceNotFoundException("user not found"));

    List<GrantedAuthority> auth = new ArrayList<>();

    return new org.springframework.security.core.userdetails.User(
            dbUser.getEmail(),
            dbUser.getPassword(),
            auth
    );
}
##3. If User Implements UserDetails

If your User class implements UserDetails, then you can directly return the user object.

User user = this.userRepo.findByEmail(username);

if (user == null) {
    throw new ResourceNotFound("user not found");
}

return user;
## 4. Security Configuration (MyConfig)
@EnableWebSecurity
@Configuration
public class MyConfig {

    @Autowired
    CustomUserDetailsService customUserDetailsService;

    @Bean
    public BCryptPasswordEncoder passwordEncorder() {
        return new BCryptPasswordEncoder();
    }

    // Configure custom UserDetails
    @Bean
    public AuthenticationProvider authenticationProvider() {
        DaoAuthenticationProvider daoAuthenticationProvider = new DaoAuthenticationProvider();
        daoAuthenticationProvider.setUserDetailsService(customUserDetailsService);
        daoAuthenticationProvider.setPasswordEncoder(passwordEncorder());
        return daoAuthenticationProvider;
    }

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests(authorize ->
                authorize.requestMatchers("/test").authenticated()
                        .anyRequest().permitAll()
        ).csrf().disable();

        return http.build();
    }

    // Used to verify user authentication
    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration config) throws Exception {
        return config.getAuthenticationManager();
    }
}
## 5. Controller (Using AuthenticationManager)
@Autowired
AuthenticationManager authenticationManager;

@PostMapping("/login")
public ResponseEntity<String> login(@RequestBody Login authRequest) throws AuthenticationException {

    Authentication authentication = authenticationManager.authenticate(
            new UsernamePasswordAuthenticationToken(
                    authRequest.getEmail(),
                    authRequest.getPassword()
            )
    );

    return ResponseEntity.ok("Login successful!");
}
## 6. Controller (Without AuthenticationManager)
@Autowired
CustomUserDetailsService customeUserDetailsService;

@PostMapping("/login")
public ResponseEntity<User> login(@RequestBody Login data) {

    Authentication authentication = authenticate(data.getEmail(), data.getPassword());

    System.out.println(authentication.getName());

    User user = this.userRepository.findByEmail(authentication.getName());

    return new ResponseEntity<>(user, HttpStatus.OK);
}

private Authentication authenticate(String username, String password) {

    UserDetails userDetails = this.customeUserDetailsService.loadUserByUsername(username);

    if (userDetails == null) {
        throw new BadCredentialsException("invalid user and password");
    }

    if (!passwordEncorder.matches(password, userDetails.getPassword())) {
        throw new BadCredentialsException("invalid password");
    }

    return new UsernamePasswordAuthenticationToken(userDetails, null, null);
}
## ✅ Summary

UserDetails → Interface for Spring Security user

UserDetailsService → Load user from database

AuthenticationProvider → Validates user credentials

AuthenticationManager → Handles authentication process

Two login approaches:
With AuthenticationManager (recommended)

Manual authentication (custom logic)




## JWT Authentication
#3 dependency
1. this is interface which has all method only
 <dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-api</artifactId>
    <version>0.11.5</version>
</dependency>

2. this is interface class where all method are overridden (core logic).
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-impl</artifactId>
    <version>0.11.5</version>
</dependency>

3. jwt deal with JSON. This class converts that header (Algorithm & Token Type), payload (User Data (Claims)), and signature(Security/Validation)  into JSON format. Simple all authentication credentials in JSON format when creating JWT authentication, sending time
   when request come jackson will convert that request into an object again.
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-jackson</artifactId>
    <version>0.11.5</version>
</dependency>

class
1. JwtAuthenticationEntryPoint -> show message when an exception come.
2. JwtAuthenticationFilter -> fetch data from the header set into the securityContextHolder
3. JwtHelper  -> actual core logic



3. JwtHelper

   like first open tool box (parseBilder() (kholna))  with secret key (unlock system) .build() means system ready to work, 
   parseClaimsJwt take token and convert into object and return.
   ```
    Claims getClaimsFromToken(String token) {
		return  Jwts.parserBuilder().setSigningKey(secretKey).build().parseClaimsJws(token).getBody();	
	}
```


ye check karta hai ki kya expire date avi date se badh ki date hai, (if yes then return true)
```
 public  boolean validateToken(String token,UserDetails userDetails) {
  	if(getUsernameFromToken(token).equals(userDetails.getUsername())) {

  		if(getAllClaims(token).getExpiration().after(new Date())) {
  	
  			return true;
  		}
  	}
  	return false;
  }
```

parserBuild -> kholna
build -> Banana (create)

``` public String generateToken(UserDetails userDetails) {
  	return Jwts.builder().setSubject(userDetails.getUsername())
  			.setIssuedAt(new Date(System.currentTimeMillis()))
  			.setExpiration(new Date(System.currentTimeMillis()+5*60*60*1000))
  			.signWith(key, SignatureAlgorithm.HS512)
  			.compact();
  }

```
