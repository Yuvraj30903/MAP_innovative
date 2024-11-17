# Use an official Node.js runtime as the base image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Set environment variables for Eureka
# Set these environment variables when running the Docker container, or adjust them as needed
ENV EUREKA_HOST=discovery-server
ENV EUREKA_PORT=8761
ENV EUREKA_APP_NAME=book-recommendation-service
ENV EUREKA_PORT_APP=8082

# Expose the application port
EXPOSE 8082

# Command to run the service
CMD ["node", "index.js"]
