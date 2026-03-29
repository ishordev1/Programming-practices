# Spring Boot Development Notes 🚀

Summary of key Spring modules, architectures, and database relationship handling.

---

## 🍃 Spring Framework Core Concepts

### 1. Inversion of Control (IoC)
IoC ek fundamental concept hai jahan control (object creation aur management ka) programmer se framework (Spring Container) ko transfer ho jata hai.
**IoC ke 3 main kaam hote hain:**
* **Object Creation**: Objects (Beans) ko instantiate karna.
* **Management**: Objects ki lifecycle ko manage karna.
* **Dependency Injection (DI)**: Ek object ki dependencies ko doosre object mein inject karna.



### 2. @RestController vs @Controller
| Feature | @Controller | @RestController |
| :--- | :--- | :--- |
| **Response** | Usually used for Web Pages (View Resolver). | Used for REST APIs (JSON/XML). |
| **Annotation** | Requires `@ResponseBody` on methods. | `@Controller` + `@ResponseBody` combined. |

### 3. Why use DTO (Data Transfer Object)?
* **Data Security**: Sensitive data (jaise passwords) ko API response se hide karne ke liye.
* **Formatted Response**: API response ko clean rakhne aur unnecessary nesting (avoiding infinite loops) se bachne ke liye.
* **Decoupling**: Entity structure aur API contract ko alag rakhne ke liye.

---

## 🔐 Spring Security & JWT
Building secure authentication using JSON Web Tokens.
* **Authentication**: User identity verify karna.
* **Authorization**: User permissions check karna.
* **JWT Filter**: Har request ke header se token validate karna.

---

## 🔄 Many-to-Many Mapping
Many-to-Many relationship mein ek **Bridge Table** (Join Table) create hoti hai.

### ✅ Entity Implementation
```java
@ManyToMany
@JoinTable(
    name = "product_category",
    joinColumns = @JoinColumn(name = "product_id"),
    inverseJoinColumns = @JoinColumn(name = "category_id")
)
List<Category> categories;


```



🧪 Accessing Data with Spring Data JPA
Bridge table ke data ko access karne ke liye EntityField_PropertyName pattern use hota hai.

From ProductRepo: List<Product> findByCategories_Id(String categoryId);

From CategoryRepo: List<Category> findByProducts_Id(String productId);

📝 Note: Nested ID access karne ke liye underscore _ ka use karein (e.g., categories_Id).

🔗 Product Unlink from Bridge Table
Delete karne se pehle relationships ko clear karna zaroori hai taaki bridge table clean rahe.

Java
public void deleteProduct(String productId) {
    Product product = productRepository.findById(productId)
            .orElseThrow(() -> new ResourceNotFoundException("Product not found"));
            
    // Clear relationships to clean join table
    product.getCategories().forEach(cat -> cat.getProducts().remove(product));
    
    productRepository.delete(product);
}

# 👨‍👩‍👧 One-to-Many (Parent) & Many-to-One (Child)
1. Many-to-One (Standard Approach) - No Extra Table
Hibernate extra table nahi banata. Child table mein ek Foreign Key column add ho jata hai.
default behavour: lazyloading

Java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "subcategory_id")
private Subcategory subcategory;
# 2. One-to-Many (Unidirectional) - Extra Table
Agar child mein @ManyToOne nahi hai, toh Hibernate default mein ek Join Table bana deta hai kyunki use nahi pata hota ki column kahan add karna hai.

# 3. Bidirectional Mapping (Best Practice)
mappedBy ka use karke extra table banne se roka jata hai.

Java
@OneToMany(mappedBy = "category")
private List<Product> products = new ArrayList<>();








