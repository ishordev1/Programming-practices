# spring module
- build spring security with jwt token
- what is IOC?
- it has 3 work--> create object , management and dependency injection rest controller vs controller

# why use Dto?
- > To make secure the data (password means, import data)  and API Response Formatted (avoid the nested).

# Many-to-Many Mapping
- create extra table  called bridge table.
- to access the the data of Bridge table use  EntityField_EntityField which present in entity.
```
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
```

# call External api using Restclient
<img width="1462" height="662" alt="image" src="https://github.com/user-attachments/assets/e3cd59cc-12ae-4072-895b-ff7e34bda632" />

# Data Extract from response
- we can extract data using 2 or 3 type
- 1. desing Dto same like json, it automatic get data or ignore remaining field
- - if use dto then use
  - record is new class you can also use simple class
```
package com.kaivalkids.shiprocket.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)

public record CourierCompany(
        @JsonProperty("courier_company_id")
        int id,
        
        @JsonProperty("courier_name")
        String name,
        
        double rate,
        double rating,
        
        @JsonProperty("estimated_delivery_days")
        String estimatedDeliveryDays,
        
        @JsonProperty("etd")
        String estimatedDeliveryDate,
        
        @JsonProperty("is_surface")
        boolean isSurface,
        
        int cod
) {}
```

	- 2. direct but bliend using JsonNode
```
	public void extractImportantData(String orderId) {
    String token = getToken();

    // 1. Directly JsonNode me response le lo (Koi custom class nahi chahiye)
    JsonNode response = restClient.get()
            .uri(shipRocketApiUrl + "/courier/serviceability?order_id=" + orderId)
            .header("Authorization", "Bearer " + token)
            .retrieve()
            .body(JsonNode.class);

    // 2. Direct path se 'available_courier_companies' ki list nikal lo
    JsonNode couriers = response.path("data").path("available_courier_companies");

    // 3. Loop chalakar jo field chahiye extract kar lo
    if (couriers.isArray()) {
        for (JsonNode courier : couriers) {
            String name = courier.path("courier_name").asText();
            double rate = courier.path("rate").asDouble();
            double rating = courier.path("rating").asDouble();
            String edd = courier.path("estimated_delivery_days").asText();

            System.out.println("Courier: " + name + " | Rate: " + rate + " | Rating: " + rating + " | Days: " + edd);
        }
    }
}
```

# Product unlink from bridge table

```
public void deleteProduct(String productId) {
		 Product product = productRepository.findById(productId)
			        .orElseThrow(() -> new ResourceNotFoundException("Product not found"));
			    // Optional: clear product from categories (to clean join table)
			    product.getCategories().forEach(cat -> cat.getProduct().remove(product));
			    productRepository.delete(product);
	}
```
------------------------------------------------------------------------

# OneToMany (Parents) and ManyToOne(Child)

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



# Spring Data JPA Specification (Filter System)
## JPA Query
- it fetch data with different entity but return on single dto, not nested dto
- eg: product-> variant-> inventory ------------------Data fetch from product, variant inventory----------
  	- it return one class not ProudctDto not data in varinat & inventory
  	- means child is blank
- 
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



### How to implement Specification in Project
- just in Repository also extends jpaSpecificationExecutor and pass entity
  ```
  public interface ProductRepository extends JpaRepository<Product, String> ,JpaSpecificationExecutor<Product> {
  }
  ```
- create specification package and make SpecificationDto class
- eg: ProductFilterSpeficicationDto
- Create method in that class.
- Only check it null or not and put in list after convert that list into predicate.
- predicates.add(cb.equal(root.get("wholesaler").get("id"), filter.getWholesalerId()));
- root.get("wholesaler") <-- this wholesaler is entity field 
-  filter.getWholesalerId() <-- this dto which want to compare.
-  if entity have any list variable, first fetch that variable entity using then work
```
 Join<Product, ProductAttribute> attributeJoin =
				            root.join("productAttributes");

				    predicatesList.add(
				        cb.and(
				            cb.equal(
				                cb.lower(attributeJoin.get("name")),
				                "color"
				            ),
				            attributeJoin.get("value")
				                         .in(filter.getColors())
				        )
				    );
```

```
package com.kaivalkids.specification;

import java.util.ArrayList;
import java.util.List;

import org.jspecify.annotations.Nullable;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.util.StringUtils;

import com.kaivalkids.dto.FilterProductByUserDto;
import com.kaivalkids.dto.ProductFilterByAdminDto;
import com.kaivalkids.model.Product;

import jakarta.persistence.criteria.CriteriaBuilder;
import jakarta.persistence.criteria.CriteriaQuery;
import jakarta.persistence.criteria.Predicate;
import jakarta.persistence.criteria.Root;

public class ProductSpecification {

	public static Specification<Product> filterProductsByAdmin(ProductFilterByAdminDto filter) {
//root for accessing entity attributes, query for building the query, and cb for constructing predicates.
//query is use to build the query and can be used for things like ordering or grouping,
		// while cb is used to create predicates that represent the conditions of the
		// query.
//cb is use for conditions like "like", "equal", "greater than", etc.,
		// which are essential for filtering the results based on the criteria specified
		// in the filter object.

		return (root, query, cb) -> {

			List<Predicate> predicates = new ArrayList<>();
			// this means predicates and it will added into the list.
			if (StringUtils.hasText(filter.getSearch())) {
				predicates.add(cb.like(cb.lower(root.get("name")), "%" + filter.getSearch().toLowerCase() + "%"));
			}

			if (filter.getActive() != null) {
				predicates.add(cb.equal(root.get("isActive"), filter.getActive()));
			}

			if (StringUtils.hasText(filter.getCategoryId())) {
				predicates.add(cb.equal(root.get("category").get("id"), filter.getCategoryId()));
			}

			if (StringUtils.hasText(filter.getSubcategoryId())) {
				predicates.add(cb.equal(root.get("subcategory").get("id"), filter.getSubcategoryId()));
			}

			if (StringUtils.hasText(filter.getWholesalerId())) {
				predicates.add(cb.equal(root.get("wholesaler").get("id"), filter.getWholesalerId()));
			}

			// cb.and means that all predicate must be true. it auto convert all predicate
			// with and condition.
			// return cb.and(predicates.toArray(new Predicate[0])); // Convert list to array
			// and return the combined predicate
			//or

			return cb.and(predicates.toArray(new Predicate[predicates.size()])); // toArray is use to convert list of
																					// predicate to array,
			// so we pass total size of blank predicate. then to array fill that blank array
			// to in that predicate
		};
	}


}

```

- In serviceImple just call that specification method and pass in that repository.

```
	@Override
	public PageableResponse<ProductDto> getAllProducts(ProductFilterByAdminDto filter, int pageNumber, int pageSize,
			String sortBy, String sortDir) {

		Sort sort = sortDir.equalsIgnoreCase("desc") ? Sort.by(sortBy).descending() : Sort.by(sortBy).ascending();

		Pageable pageable = PageRequest.of(pageNumber - 1, pageSize, sort);

		Specification<Product> specification = ProductSpecification.filterProductsByAdmin(filter);

		Page<Product> pageProduct = productRepository.findAll(specification, pageable);

		return PageableUtil.getPageableResponse(pageProduct, ProductDto.class);
	}
```

## Sometime we dont expose data for user like we have Stock and reserveStock for user we show only Available stock we dont have field available in admin side.
	- Just make create method in entity it does not expose the data. 
	- user entity add column availableQuantity
	
	```
	  @Transient
    public Integer getAvailableQuantity() {
        return quantity - reservedQuantity;
    }
	```
```
public class Inventory {

    private Integer quantity;
    private Integer reservedQuantity;

    @Transient
    public Integer getAvailableQuantity() {
        return quantity - reservedQuantity;
    }
}

public class InventoryUserResponseDto {

    private String id;
    private Integer availableQuantity;
}
```

```
{
  "id": "123",
  "availableQuantity": 15
}
```




Case 1: Simple Field

If the field is:

private String brand;

then:

root.get("brand")

✅ Works directly.

Case 2: ManyToOne
@ManyToOne
private Category category;

You can do:

root.get("category").get("name")

✅ Usually works.

Example:

root.get("category")
    .get("id")
    .in(filter.getCategoryIds());
Case 3: OneToMany / List
@OneToMany
private List<ProductAttribute> productAttributes;

Now:

root.get("productAttributes")

returns a collection.

You cannot do:

root.get("productAttributes")
    .get("value")

❌ Error / Invalid

Because JPA doesn't know which item in the list you mean.

So you must join:

Join<Product, ProductAttribute> attributeJoin =
        root.join("productAttributes");

Then:

attributeJoin.get("value")

