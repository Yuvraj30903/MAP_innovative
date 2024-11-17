# Stage 1: Build the application
FROM maven:3.8.8-eclipse-temurin-17 AS build

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY pom.xml .
COPY src ./src

# Build the application using Maven
RUN mvn clean package -DskipTests

# Stage 2: Create the runtime image
FROM eclipse-temurin:17-jdk-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the JAR file from the build stage
COPY --from=build /app/target/app-0.0.1-SNAPSHOT.jar /app/app-0.0.1-SNAPSHOT.jar

# Expose the port that the app will run on
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "app-0.0.1-SNAPSHOT.jar"]
