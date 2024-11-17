const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const natural = require('natural');

const app = express();
app.use(bodyParser.json());
const { registerWithEureka } = require('./eureka');
const API_GATEWAY_URL = 'http://api-gateway:8080';  
// Example database of books
let allBooks = [];

// Helper function to find similar books
async function fetchAllBooks()
{
    const response = await axios.get(`${API_GATEWAY_URL}/api/book/`);
    allBooks = response.data;
    console.log(response.data)
}
function findSimilarBooks(book, allBooks) {
    const tokenizer = new natural.WordTokenizer();
    const bookTokens = tokenizer.tokenize(book.description.toLowerCase());

    return allBooks.filter(b => {
        if (b.bookId === book.bookId) return false; // Exclude the original book
        const otherTokens = tokenizer.tokenize(b.description.toLowerCase());
        const similarity = natural.JaroWinklerDistance(bookTokens.join(" "), otherTokens.join(" "));
        return similarity > 0.5; // Threshold for similarity
    });
}

// Endpoint for book recommendations
app.get('/recommand/:id', async (req, res) => {
    const { id } = req.params;

    try {
        // Fetch the book details from the API Gateway
        const response = await axios.get(`${API_GATEWAY_URL}/api/book/${id}`);
        const book = response.data;
        console.log(book);
        console.log("here");
        // Find similar books
        const recommendations = findSimilarBooks(book, allBooks);

        res.json({
            book,
            recommendations,
        });
    } catch (error) {
        console.error(error.message);
        res.status(500).json({ error: 'Failed to fetch book data or recommendations' });
    }
});

// Start the service
const containerIpAddr = process.env.CONTAINER_IP || '127.0.0.1'; // Can be adjusted to the Docker network IP

const PORT = process.env.EUREKA_PORT_APP || 8082;
registerWithEureka((error) => {
    if (error) {
      console.error('Error registering with Eureka');
    }
  
    // Start the Express server only after registration with Eureka is successful
});
app.listen(PORT, () => {
    console.log(`Book Recommendation Service listening at http://${containerIpAddr}:${PORT}`);
});
fetchAllBooks()
  