# First make .env file for dynamic value in sts in parents directory, meaning below the pom.xml
```
# Spring Boot
DB_URL=jdbc:postgresql://postgres:5432/TEST
DB_USERNAME=postgres
DB_PASSWORD=root
JPA_DDL_AUTO=update
JPA_SHOW_SQL=true
# PostgreSQL Container
POSTGRES_DB=TEST
POSTGRES_USER=postgres
POSTGRES_PASSWORD=root
FRONTEND_URL=http://localhost:3000
jwt.secret=saiofal;vkasfbehwqpofhjashofjaswfpojasfvbafop[hfifonfo[shjfwefjjfslajfsahfoshffasnbash[f
jwt.access-ttl-seconds=86400

jwt.refresh-ttl-seconds=86400
jwt.issuer=api.substring.com
 
jwt.refresh-token-cookie-name=refreshToken
jwt.cookie-secure=false
jwt.cookie-http-only=true
jwt.cookie-same-site=lax
jwt.cookie-domain=localhost
spring.security.oauth2.client.registration.google.client-id=****
spring.security.oauth2.client.registration.google.client-secret=****
auth2.success-redirect-url=http://localhost:3000/success
auth2.failure-redirect-url=http://localhost:3000/signin
```

# dockerfile
```
# ------------ BUILD STAGE ------------

FROM maven:3.9.6-eclipse-temurin-17 AS build

WORKDIR /app

# Copy pom.xml and download dependencies
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Copy source code
COPY src ./src

# Package the application
RUN mvn clean package -DskipTests


# ------------ RUN STAGE ------------
FROM eclipse-temurin:17-jdk

WORKDIR /app

# Copy jar from build stage
COPY --from=build /app/target/*.jar app.jar

# Render sets PORT automatically
EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

# Docker compose
```
version: "3.9"

services:
  postgres:
    image: pgvector/pgvector:pg17
    container_name: kaivalkids-postgres
    restart: unless-stopped

    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}

    ports:
      - "5432:5432"

    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build:
      context: .
      dockerfile: Dockerfile

    container_name: kaivalkids-backend
    restart: unless-stopped

    env_file:
      - .env

    depends_on:
      - postgres

    ports:
      - "8080:8080"

volumes:
  postgres_data:
```

# command to run docker compose
1. docker compose build
2. docker compose up -d
3. docker ps             <------- check
4. docker compose logs -f backend     <- check logs



