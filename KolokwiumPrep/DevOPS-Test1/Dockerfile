FROM maven:3.9.6-eclipse-temurin-17 AS builder

WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=builder /app/target/main-1.0-jar-with-dependencies.jar app.jar

ENV MESSAGE="To jest komunikat testowy"

ENTRYPOINT ["java", "-jar", "app.jar"]