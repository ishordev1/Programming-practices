# spring module
- build spring security with jwt token
- what is IOC?
- it has 3 work--> create object , management and dependency injection rest controller vs controller

# why use Dto?
- > To make secure the data (password means, import data)  and API Response Formatted (avoid the nested).
--------------------------------------------------🔁 Many-to-Many Mapping------------------------------------------------

 - > create extra table  called bridge table.
- >  to access the the data of Bridge table use  EntityField_EntityField which present in entity.

✅ In Entity
@ManyToMany
@JoinTable(name = "product_category",
joinColumns = @JoinColumn(name = "product_id"),
inverseJoinColumns = @JoinColumn(name = "category_id"))
List<Category> categories;
🧪 Accessing Data with Spring Data JPA
✅ From ProductRepo
List<Product> findByCategories_Id(String categoryId);
✅ From CategoryRepo
List<Category> findByProducts_Id(String productId);
📝 Use underscore _ to access nested ID:
categories.id → categories_Id
products.id → products_Id
-----------------------------------------Product unlink from bridge table---------------------------------------------
public void deleteProduct(String productId) {
		 Product product = productRepository.findById(productId)
			        .orElseThrow(() -> new ResourceNotFoundException("Product not found"));
			    // Optional: clear product from categories (to clean join table)
			    product.getCategories().forEach(cat -> cat.getProduct().remove(product));
			    productRepository.delete(product);
	}
------------------------------------------------------------------------

OneToMany (Parents) and ManyToOne(Child)

1. ManyToOne (Standard Approach) - No Extra Table
Jab aap @ManyToOne use karte hain, toh Hibernate extra table nahi banata. 
Iski jagah, child table (jaise products) mein ek Foreign Key column add ho jata hai jo parent table (jaise categories) ko point karta hai.
@ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "subcategory_id")
    private Subcategory subcategory;

2. OneToMany (Unidirectional) - Extra Table (Join Table)
Agar aap sirf @OneToMany use karte hain parent entity mein aur child mein @ManyToOne nahi lagate (Unidirectional),
toh Hibernate default mein ek Join Table bana deta hai.

  Kyu? Kyunki Hibernate ko nahi pata ki child table mein column kahan add karna hai, isliye wo ek link table bana deta hai.

 @OneToMany(mappedBy = "category")
    private List<Product> products = new ArrayList<>();


why initilize empty object in entity? why not direct variable initiate and work?
with initilize      -------> private List<Product> products = new ArrayList<>();
without initilize   -------> private List<Product> products;

if initilize - --> because in serviceImpl direct we can work without initilize everytime if adding new product.
if not ----> one by one initilize and do operation




-----------------



# Spring Data JPA Specification
- It is use to create advance filter method in springboot.
## Why need this?
- if we use simple repository, and try to create 5 or 10 or more column query at an simgle method, Simple JPA Repository become massey code. 
- so jpa specification can use.

### Root, Query, CriteriaBuilder Kya Hain?
1. Root → Ye table ka reference hai. Jaise aap table mein column access karte ho (root.get("price"))
2. CriteriaBuilder (cb) → Ye conditions banane ka tool hai. Jaise:
- cb.equal() → equal to condition
- cb.greaterThan() → greater than condition
- cb.like() → pattern matching condition
- cb.conjunction() → always true (ignore filter)
3. Query → Advanced queries ke liye (group by, order by), filhal ignore karo


