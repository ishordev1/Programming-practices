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
```
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

## BioDirection Mapping Only need if you Want to get data in to dual side
✅ Summary

@JsonManagedReference / @JsonBackReference → Prevent infinite recursion

Cascade → Parent actions affect child

@PathVariable vs @RequestParam → Different ways to get request data

nullable = true → Allows foreign key to be null

CommandLineRunner → Runs code at application startup






# Why we use service instant of serviceImpl why not direct use serviceimpl?
## 1. The Interface (Common Contract)Sabse pehle hum ek generic interface banate hain. Controller ko sirf isi se matlab hai:
 public interface PaymentService {
    String processPayment(double amount);
}
## 2. Multiple ImplementationsAb hum do alag-alag logic likhte hain. Dono same interface ko follow karenge:Java@Service("paytmService") // Humne iska ek specific naam de diya
public class PaytmPaymentServiceImpl implements PaymentService {
    @Override
    public String processPayment(double amount) {
        return "Processing ₹" + amount + " via Paytm (India Gateway)";
    }
}

@Service("stripeService")
public class StripePaymentServiceImpl implements PaymentService {
    @Override
    public String processPayment(double amount) {
        return "Processing $" + amount + " via Stripe (Global Gateway)";
    }
}
## 3. Deep Concept:
Runtime Selection Kaise Hoti Hai?Agar aap direct @Autowired karenge, toh Spring confuse ho jayega ki kaunsi wali use karni hai (isko NoUniqueBeanDefinitionException kehte hain).Isko solve karne ke liye hum PaymentFactory ya Registry pattern use karte hain:Method A: Using Map Injection (The Smart Way)Spring Boot ki ek bahut cool quality hai—agar aap ek Map mein interface inject karte hain, toh Spring saari implementations ko us map mein bhar deta hai (Bean name as key).Java@Service
public class PaymentFactory {

    // Spring automatically saari PaymentService ki beans is map mein daal dega
    @Autowired
    private Map<String, PaymentService> paymentMethods;

    public PaymentService getPaymentMethod(String countryCode) {
        if ("IN".equalsIgnoreCase(countryCode)) {
            return paymentMethods.get("paytmService");
        } else {
            return paymentMethods.get("stripeService");
        }
    }
}
## 4. Controller mein use kaise karein? (No If-Else)Ab dekhiye aapka Controller kitna saaf (clean) ho jayega. Use ye tension nahi leni ki payment kaise ho rahi hai:Java@RestController
public class PaymentController {

    @Autowired
    private PaymentFactory paymentFactory;

    @PostMapping("/pay")
    public String pay(@RequestParam double amount, @RequestHeader String country) {
        // Runtime par decide ho raha hai kaunsi service call hogi
        PaymentService service = paymentFactory.getPaymentMethod(country);
        return service.processPayment(amount);
    }
}
##  5. Deep Benefits (Kyun ye "Deep" hai?)Open-Closed Principle (SOLID):
Kal ko agar aapko PayPal add karna hai, toh aapko Controller ya Factory ko touch karne ki zaroorat nahi hai. Bas ek nayi PaypalPaymentServiceImpl class banaiye aur Factory mein ek line add kar dijiye.Environment Specific Beans: Aap @Profile("dev") ya @Profile("prod") use karke bhi beans switch kar sakte hain. Jaise Dev mode mein MockPaymentService aur Prod mein RealStripeService.Conditional Loading: Aap @ConditionalOnProperty use kar sakte hain. Maan lijiye aapne application.properties mein likha payment.gateway=paytm, toh Spring sirf Paytm wali bean banayega, doosri ko memory mein load hi nahi karega.Comparison: Direct Class vs Factory StrategyFeatureDirect Class (No Interface)Interface StrategyNew Payment MethodController mein bada switch-case likhna padega.Bas ek nayi class add karni hai.MemorySaara logic hamesha load rehta hai.Sirf required implementation active rehti hai.TestingHar gateway ke liye alag controller test chahiye.Ek hi test case saare gateways ke liye kaam karega.


# If want to save also child when save parents then must link with that child entity, not dto. 
👉 Save parent + child together using one .save()

Example:

Product → Variant → Image
🔑 Core Rules (REMEMBER THESE)
✅ Rule 1: Use Cascade
@OneToMany(mappedBy = "product", cascade = CascadeType.ALL)

👉 Allows saving child automatically

✅ Rule 2: Set relationship BOTH sides
child.setParent(parent);        // REQUIRED (DB)
parent.getChildren().add(child); // REQUIRED (Java memory)
✅ Rule 3: Save only parent
parentRepository.save(parent);



-> code clean, flexibility etc.
