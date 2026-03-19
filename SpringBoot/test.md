# Spring Boot Notes

## 1. JSON Management

- **Parent Side** → `@JsonManagedReference`  
- **Child Side** → `@JsonBackReference`

These annotations help to handle bidirectional relationships and avoid infinite recursion during JSON serialization.

---

## 2. Cascade Usage

When an operation is performed on the parent, it will also affect the child.

```java
@OneToOne(mappedBy = "user", cascade = CascadeType.ALL, orphanRemoval = true)



cascade = CascadeType.ALL → All operations (save, delete, update) will be applied to the child.

orphanRemoval = true → If the child is removed from the parent, it will be deleted from the database.

## 3. @PathVariable vs @RequestParam
@PathVariable

Used to fetch values from the URL path.

Example:

/user/1
@GetMapping("/user/{id}")
public User getUser(@PathVariable int id) {
    return userService.getUser(id);
}
@RequestParam

Used to fetch values from query parameters.

Example:

/user?id=2332
@GetMapping("/user")
public User getUser(@RequestParam("id") int id) {
    return userService.getUser(id);
}
## 4. @JoinColumn(nullable = true)
@JoinColumn(name = "", nullable = true)

nullable = true means the foreign key can store NULL values.

Use Case:

If a user places an order and later deletes their account, we can still keep the order history.

User → Deleted

Order → Still exists (foreign key becomes NULL)

This helps admins view past data even if the parent entity is removed.

## 5. CommandLineRunner

CommandLineRunner runs automatically after the main method executes.
It is useful for initializing data when the application starts.

Ways to Use:

By implementing CommandLineRunner

By defining a @Bean

Example Code:
@SpringBootApplication
public class AuthBackend implements CommandLineRunner {

    @Bean
    public CommandLineRunner commandLineRunner() {
        return (args) -> {
            System.out.println("This is bean command line runner");
        };
    }

    @Override
    public void run(String... args) throws Exception {

        // Create default roles

        // ADMIN Role
        roleRepository.findByName("ROLE_" + AppConstants.ADMIN_ROLE)
            .ifPresentOrElse(role -> {
                System.out.println("Admin Role Already Exists: " + role.getName());
            }, () -> {
                Role role = new Role();
                role.setName("ROLE_" + AppConstants.ADMIN_ROLE);
                role.setId(UUID.randomUUID());
                roleRepository.save(role);
            });

        // GUEST Role
        roleRepository.findByName("ROLE_" + AppConstants.GUEST_ROLE)
            .ifPresentOrElse(role -> {
                System.out.println("Guest Role Already Exists: " + role.getName());
            }, () -> {
                Role role = new Role();
                role.setName("ROLE_" + AppConstants.GUEST_ROLE);
                role.setId(UUID.randomUUID());
                roleRepository.save(role);
            });
    }
}
✅ Summary

@JsonManagedReference / @JsonBackReference → Prevent infinite recursion

Cascade → Parent actions affect child

@PathVariable vs @RequestParam → Different ways to get request data

nullable = true → Allows foreign key to be null

CommandLineRunner → Runs code at application startup
