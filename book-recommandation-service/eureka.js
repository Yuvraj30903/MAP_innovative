const Eureka = require('eureka-js-client').Eureka;

// Get environment variables for Eureka server
const eurekaHost = process.env.EUREKA_HOST || 'localhost';
const eurekaPort = process.env.EUREKA_PORT || 8761;
const appName = process.env.EUREKA_APP_NAME || 'book-recommandation-service';
const appPort = process.env.EUREKA_PORT_APP || 8082;
const containerHostName = process.env.HOSTNAME || 'book-recommandation-service';  // Dynamically set container name
const containerIpAddr = process.env.CONTAINER_IP || '127.0.0.1'; // Can be adjusted to the Docker network IP


const client = new Eureka({
  eureka: {
    host: eurekaHost,   // Eureka server hostname
    port: eurekaPort,   // Eureka server port
    servicePath: '/eureka/apps/',  // Path for registering apps
  },
  instance: {
    app: appName,         // Name of your service
    hostName: containerHostName, // Hostname for your service
    ipAddr: containerIpAddr,  // IP address of your service
    port: {
      '$': appPort,       // Port your Node.js app is running on
      '@enabled': 'true'
    },
    vipAddress: appName,  // VIP for your service
    dataCenterInfo: {
      '@class': 'com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo',
      name: 'MyOwn'
    }
  }
});

// Register the service with Eureka
const registerWithEureka = (callback) => {
    client.start(error => {
      if (error) {
        console.error('Failed to register with Eureka:');
      } else {
        console.log('Successfully registered with Eureka');
      }
      callback(error);  // Call the callback once registration is complete
    });
  };
  
  module.exports = { registerWithEureka };
  