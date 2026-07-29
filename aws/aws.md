# Connect with EC2 Server
- open folder where  you save key and open terminal in that folder
- type command : ssh -i key-file-Name server-user-name@public-ip
  ```
  ssh -i kaivalkids-ec2.pem ec2-user@13.235.81.213
  ```
  - Note: user name is alway same for all linux server
    <img width="706" height="267" alt="image" src="https://github.com/user-attachments/assets/69fa437d-f0de-4a39-a54c-4089b2353c29" />
 

# create user
- go in iam -> iam user
- first create policy and thhen add in that user
- after choose policy which created and select for that user.

<img width="1905" height="932" alt="image" src="https://github.com/user-attachments/assets/66111cd5-6cf0-411d-802a-85390cb5d317" />

### for image upload first generate sign url, and using that send put request, file select in body -> select binary and image (image name can be same name of url name)

# Create Access key and secreat key for that user to use
<img width="1537" height="337" alt="image" src="https://github.com/user-attachments/assets/c564fb19-6238-412e-b1e9-1963aaa483c9" />


 # s3 bucket has also setup cors origin 
- in your bucket -> permission -> cors origin -> edit ->
- search from googl -> s3 bucket cors origin resource ->  copy from anyother website
 ```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "http://www.example1.com"
        ],
        "ExposeHeaders": []
    },
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "http://www.example2.com"
        ],
        "ExposeHeaders": []
    },
    {
        "AllowedHeaders": [],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```


# Creating Database search Aurora and RDS   ----> here you choose any database, like sql, postgresql etc
- bydefault all are private and secure
- for location connection  make it public and it inbound and outbound make public
- 
