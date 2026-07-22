# First check you jar file run in local system
- .\mvnw clean package -DskipTests  <-- this command build jar without  run in when build jar,  skip run because some time env file not found in local

<img width="1017" height="581" alt="image" src="https://github.com/user-attachments/assets/9ceebcb8-f3d9-45ee-b600-e70f703d111d" />


# Docker
- Dockerfile -> compile and build  it become -> Docker Image -> run image it become -> Docker Container
# Dockerfile, Docker Compose
- DockerCompose<- If we have multiple Dockerfile we need docker compose to manage it.

  
- enable hypervisor plateform -> search--> turn on window feature
1. check window window hypervisor plateform and also
2. window subsystem for linux

- and restart system
- login in docker

- Now ready your system to Install to Docker

  --------
### Check Docker is install or not open cmd
- docker -v      <------------ check version

- Note: After create docker image you dont see that using file explorer, only see using docker gui or command,
- to see that file open cmd anywhere run --->  docker images

--------------------------
# IN Short
- docker images     <-------- to check image
- docker build -t myapp . <- Docker file to image "myapp" <-- put any name you want to make your image
- docker run myapp      <--------this run that image
- docker ps       <-  it show running container
- docker stop dockerId    <- this stop running container
- docker rm -f myapp     <---- force remove container
- docker rmi -f myapp     <---- force remove that image


-------------------------



  
## Docker command open cmd and use docker or gui
- it download docker image from docker hub and give response
<img width="1473" height="385" alt="image" src="https://github.com/user-attachments/assets/2e4f1cd3-71a7-401f-9741-4022f7eb2e3d" />

- Docker Hub is official website where store all deploy image from there we can use any image or store personal image in there
<img width="1318" height="475" alt="image" src="https://github.com/user-attachments/assets/0e4be337-e444-4b28-8914-56ff51bebeb0" />


- to see the work follow or command
<img width="680" height="85" alt="image" src="https://github.com/user-attachments/assets/fba05b40-d54a-4681-b053-dea8613735e6" />

## some docker command
<img width="1536" height="1024" alt="ChatGPT Image Jul 20, 2026, 10_11_57 AM" src="https://github.com/user-attachments/assets/3dac002c-31e8-4340-8824-3c6e96f7c332" />

## prepare for springboot file
<img width="1024" height="1536" alt="ChatGPT Image Jul 20, 2026, 08_55_29 AM" src="https://github.com/user-attachments/assets/f433b89f-4b63-4505-8bad-8b34cb6a94e2" />



# Springboot Deployment

<img width="1451" height="1083" alt="image" src="https://github.com/user-attachments/assets/1755a9dd-895e-4fe3-ac18-cab9c9524674" />

# how to connect cloud computer with local
- download github
- use this commant
  ```
   ssh -i kaivalkids-server.pem ec2-user@13.204.83.163
  ```
- kaivalkids-server.pem <- thsi is ssh-key-file-name-with-extension
- ec2-user@    <- this is ec2 user name alway same
- 13.204.83.163 <- this is server(ec2) public id copy from server

<img width="1362" height="715" alt="image" src="https://github.com/user-attachments/assets/e7ec8866-4f41-4304-b354-88768f053e4b" />


# build ci/cd pipline
- github have multiple action in marketplace use to that action for building ci/cd code.

### Workflow Steps

1. Checkout code
2. Setup Java
3. Build a jar
4. Login dockerhub
5. Build image
6. push image
7. Deploy to ec2 using SSH

```
name: Java CI/CD Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    # 1. Checkout code
    - name: Checkout code
      uses: actions/checkout@v4

    # 2. Setup Java
    - name: Setup Java
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'

    # 3. Build a jar
    - name: Build a jar
      run: ./gradlew build # or `mvn clean package`

    # 4. Login dockerhub
    - name: Login dockerhub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}

    # 5. Build image & 6. Push image
    - name: Build and push image
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ secrets.DOCKERHUB_USERNAME }}/my-app:latest

    # 7. Deploy to ec2 using SSH
    - name: Deploy to ec2 using SSH
      uses: appleboy/ssh-action@v1.0.3
      with:
        host: ${{ secrets.EC2_HOST }}
        username: ${{ secrets.EC2_USERNAME }}
        key: ${{ secrets.EC2_SSH_KEY }}
        script: |
          docker pull ${{ secrets.DOCKERHUB_USERNAME }}/my-app:latest
          docker stop my-app || true
          docker rm my-app || true
          docker run -d --name my-app -p 80:8080 ${{ secrets.DOCKERHUB_USERNAME }}/my-app:latest
```








