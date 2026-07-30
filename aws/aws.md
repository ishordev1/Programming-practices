# Connect with EC2 Server
- open folder where  you save key and open terminal in that folder
- type command : ssh -i key-file-Name server-user-name@public-ip
  ```
  ssh -i kaivalkids-ec2.pem ec2-user@13.235.81.213
  ```
- Note: the username is always same for all amazon linux server
    <img width="706" height="267" alt="image" src="https://github.com/user-attachments/assets/69fa437d-f0de-4a39-a54c-4089b2353c29" />
 
 # Setup New EC2 server for run docker project
 - Note: if already have docker image there all things already build-in, direct setup docker and  run project
 - After Create Ec2 run this process for setup
1. Step 1: Connect to your EC2
- open folder wehre your server key are store and run terminal or git shell
```
ssh -i your-key.pem ec2-user@YOUR_EC2_PUBLIC_IP
```
2. Step 2: Update the server
```
sudo dnf update -y
```
3. Step 3: Install Docker
```
sudo dnf install docker -y
```
- Check Docker:
  ```
  docker --version
  ```
4. Step 4: Start Docker
```
sudo systemctl start docker
sudo systemctl enable docker
```
- check status
```
  sudo systemctl status docker
```
-  It should show active (running).

5. Step 5: Allow ec2-user to use Docker
```
   sudo usermod -aG docker ec2-user
```
```
   exit
```
- Reconnect to the server: --> ssh -i your-key.pem ec2-user@YOUR_EC2_PUBLIC_IP
- or rebot using this command: sudo reboot

6. Step 6: Test Docker

```
docker ps
```
- If it works without sudo, you're done.

7. Step 7: Create the folder for your .env
```
mkdir -p /home/ec2-user/personal
```

8. Step 8: Create the .env file
```
nano /home/ec2-user/personal/.env
```
- Paste all your environment variables, for example
```
DB_URL=...
DB_USERNAME=...
DB_PASSWORD=...

JWT_SECRET=...

AWS_ACCESS_KEY=...
AWS_SECRET_KEY=...

SPRING_PROFILES_ACTIVE=prod
```
- save ctrl + o and enter
-  ctrl + x and enter

9. Step 9: Configure the Security Group
- add inbound port 8080
<img width="705" height="312" alt="image" src="https://github.com/user-attachments/assets/530989c9-0d9f-412d-8d60-904ab2794760" />


###  After deploy, also allow port 8080 in inbound in ec2, because springboot running 8080 port
<img width="1648" height="342" alt="image" src="https://github.com/user-attachments/assets/2a0cfc16-86b4-48db-b009-9dcc067f5e9b" />

### For Accessing server use server public address and port
- http://13.235.81.213:8080


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
