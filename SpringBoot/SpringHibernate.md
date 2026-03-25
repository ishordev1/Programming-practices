# Spring Boot & JPA Quick Reference

### Spring Modules & Concepts
* **Spring Security**: Build authentication and authorization with JWT tokens.
* **IOC (Inversion of Control)**: It has 3 main responsibilities:
    1. Create objects.
    2. Management of object lifecycle.
    3. Dependency Injection.
* **RestController vs Controller**: 
    * `@Controller` is used for traditional web pages (MVC).
    * `@RestController` is used for RESTful web services (JSON/XML).

### Data Transfer Object (DTO)
**Why use DTO?**
* To secure sensitive data (e.g., hiding passwords or internal import data).
* To format API responses properly (avoiding deep nesting or infinite loops).

---

### 🔁 Many-to-Many Mapping
* Creates an extra table called a **Bridge Table** (Join Table).
* To access the data of the Bridge table, use the `EntityField_PropertyName` pattern.

#### ✅ In Entity
```java
@ManyToMany
@JoinTable(
    name = "product_category",
    joinColumns = @JoinColumn(name = "product_id"),
    inverseJoinColumns = @JoinColumn(name = "category_id")
)
```
List<Category> categories;
🧪 Accessing Data with Spring Data JPA
From ProductRepo: List<Product> findByCategories_Id(String categoryId);

From CategoryRepo: List<Category> findByProducts_Id(String productId);

📝 Note: Use an underscore _ to access nested IDs: categories.id → categories_Id.

----------------- Product unlink from bridge table -----------------
Java
public void deleteProduct(String productId) {
    Product product = productRepository.findById(productId)
            .orElseThrow(() -> new ResourceNotFoundException("Product not found"));

    // Optional: clear product from categories (to clean join table)
    product.getCategories().forEach(cat -> cat.getProducts().remove(product));
    
    productRepository.delete(product);
}
👨‍👩‍👧 OneToMany (Parents) and ManyToOne (Child)
1. ManyToOne (Standard Approach) - No Extra Table
Jab aap @ManyToOne use karte hain, toh Hibernate extra table nahi banata. Iski jagah, child table (jaise products) mein ek Foreign Key column add ho jata hai jo parent table (categories ya subcategories) ko point karta hai.

Java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "subcategory_id")
private Subcategory subcategory;
2. OneToMany (Unidirectional) - Extra Table (Join Table)
Agar aap sirf @OneToMany use karte hain parent entity mein aur child mein @ManyToOne nahi lagate (Unidirectional), toh Hibernate default mein ek Join Table bana deta hai.

Reason: Kyunki Hibernate ko nahi pata ki child table mein column kahan add karna hai, isliye wo ek link table create karta hai.

3. Bidirectional Mapping (Best Practice)
mappedBy use karne se extra table nahi banti.

Java
@OneToMany(mappedBy = "category")
private List<Product> products = new ArrayList<>();
