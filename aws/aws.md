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


# Now To Setup Domain with this public ip
- open your domain provider
- add there DNS Record which point you EC2 public IP. and wait 10 to 15 min.
<img width="1091" height="62" alt="image" src="https://github.com/user-attachments/assets/165ac89a-dc44-4239-8ef1-5e5d1f2a8a24" />
- Note: put ttl default what server provide

- check domain is point in your EC2 or not using this command
- nslookup kaivalkids.com
- also check in local cmd that above command, sometime in local it take time to clear cache of that DNS.


### Setup Nginx for port forwarding in your local 8080 to your Domain
- Install Nginx in ec2      -> sudo dnf install nginx -y
- start Nginx 
```
sudo systemctl enable nginx
sudo systemctl start nginx
```
- Check the status:    sudo systemctl status nginx
- It should show: Active: active (running)
- now we search our ec2 ip in browser then it  will show welcom to nginx  page, this means our nginx running

- sudo nano /etc/nginx/nginx.conf
- after open that file and replace this in place of server
- search this:
<img width="587" height="302" alt="image" src="https://github.com/user-attachments/assets/8aefa9c7-c2a0-47e0-acc5-afa1e7e810e0" />

replace this:
```
server {
    listen 80;
    server_name api.kaivalkids.com;

    location / {
        proxy_pass http://127.0.0.1:8080;

        proxy_http_version 1.1;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
- Note: instant of ip 127.0.0.1 you can also add localhost: because this ip is also localhost ip.
- save file: ctrl + 0 and enter
- ctrl + x and enter
- After save check it is correct or not
<img width="740" height="107" alt="image" src="https://github.com/user-attachments/assets/529d268e-2c71-4202-bdc1-baede08257ad" />

- reload nginx: sudo systemctl reload nginx
- check status: sudo systemctl status nginx

- now your server response in that domain (not use Https): http://api.kaivalkids.com
---
### Now install SSL for secure domain
- Step 1: Install Certbot
```
sudo dnf install certbot python3-certbot-nginx -y
```
- Step 2: Generate the SSL certificate
```
sudo certbot --nginx -d api.kaivalkids.com
```
- enter email where you want to get notification when ssl expire or any error happen
- enter yes 2 3 place
- 

 <br><br><br><br>
---
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
