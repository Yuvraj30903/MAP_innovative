from flask import Flask, request, jsonify
from models import add_book, get_books, update_book, delete_book
from database import init_db
from py_eureka_client.eureka_client import EurekaClient
app = Flask(__name__) 
import asyncio
# Initialize the database
init_db()
async def start_eureka():
    eureka_client = EurekaClient(
        eureka_server="http://discovery-server:8761/eureka/",
        app_name="book-inventory-service",
        instance_port=8083,  
        instance_ip="book-inventory-service" 
    )

    # Start Eureka registration in a separate thread
    await eureka_client.start()

asyncio.run(start_eureka())

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Book Inventory Microservice!",
        "endpoints": {
            "list_books": "/invetory (GET)",
            "add_book": "/invetory (POST)",
            "update_book": "/invetory/<bookId> (PUT)",
            "delete_book": "/invetory/<bookId> (DELETE)"
        }
    })


@app.route('/inventory', methods=['GET'])
def list_books():
    # Get query parameters from the request
    id = request.args.get('id')
    bookId = request.args.get('bookId')
    title = request.args.get('title')
    author = request.args.get('author')
    published_date = request.args.get('published_date')
    quantity = request.args.get('quantity')

    # Validate and process query parameters
    if id:
        try:
            id = int(id)
        except ValueError:
            return jsonify({"error": "'id' should be an integer."}), 400

    if bookId:
        try:
            bookId = int(bookId)
        except ValueError:
            return jsonify({"error": "'bookId' should be an integer."}), 400

    if title and not isinstance(title, str):
        return jsonify({"error": "'title' should be a string."}), 400

    if author and not isinstance(author, str):
        return jsonify({"error": "'author' should be a string."}), 400

    if published_date and not isinstance(published_date, str):
        return jsonify({"error": "'publiched_date' should be a string."}), 400

    if quantity:
        try:
            quantity = int(quantity)
        except ValueError:
            return jsonify({"error": "'quantity' should be an integer."}), 400

    # Call the `get_books` function to retrieve data based on the provided parameters
    books = get_books(
        id=id,
        bookId=bookId,
        title=title,
        author=author,
        published_date=published_date,
        quantity=quantity
    )

    # Return the response
    if books:
        return jsonify([dict(book) for book in books]), 200
    else:
        return jsonify({'error': 'No books found matching the provided parameters'}), 404


@app.route('/inventory', methods=['POST'])
def create_book():
    data = request.json 
    add_book(data['bookId'],data['title'],data['author'], data.get('published_date'), data['quantity'])
    return jsonify({'message': 'Book added successfully'}), 201


@app.route('/inventory', methods=['PUT'])
def update_existing_book():
    # Get query parameters from the request
    id = request.args.get('id')
    bookId = request.args.get('bookId')
    title = request.args.get('title')
    author = request.args.get('author')
    published_date = request.args.get('published_date')
    quantity = request.args.get('quantity')

    # Get data to update from the request body
    data = request.json
    new_id = data.get('id')
    new_bookId = data.get('bookId')
    new_title = data.get('title')
    new_author = data.get('author')
    new_published_date = data.get('published_date')
    new_quantity = data.get('quantity')

    # Validate and process query parameters
    if id:
        try:
            id = int(id)
        except ValueError:
            return jsonify({"error": "'id' should be an integer."}), 400

    if bookId:
        try:
            bookId = int(bookId)
        except ValueError:
            return jsonify({"error": "'bookId' should be an integer."}), 400

    if title and not isinstance(title, str):
        return jsonify({"error": "'title' should be a string."}), 400

    if author and not isinstance(author, str):
        return jsonify({"error": "'author' should be a string."}), 400

    if published_date and not isinstance(published_date, str):
        return jsonify({"error": "'publiched_date' should be a string."}), 400

    if quantity:
        try:
            quantity = int(quantity)
        except ValueError:
            return jsonify({"error": "'quantity' should be an integer."}), 400
        
    # Validate new data (fields to update)
    try:
        if new_id is not None:
            new_id = int(new_id)
        if new_bookId is not None:
            new_bookId = int(new_bookId)
        if new_quantity is not None:
            new_quantity = int(new_quantity)
        if new_title and not isinstance(new_title, str):
            return jsonify({"error": "'new_title' should be a string."}), 400
        if new_author and not isinstance(new_author, str):
            return jsonify({"error": "'new_author' should be a string."}), 400
        if new_published_date and not isinstance(new_published_date, str):
            return jsonify({"error": "'new_published_date' should be a string."}), 400
    except ValueError:
        return jsonify({"error": "Invalid parameter. Ensure 'id', 'bookId', 'quantity' are integers and 'published_date' is in YYYY-MM-DD format."}), 400

    # Ensure at least one query parameter is provided to identify the book(s)
    if not any([id, bookId, title, author, published_date, quantity]):
        return jsonify({"error": "At least one filter parameter (id, bookId, title, etc.) must be provided to identify the book(s)."}), 400

    # Ensure at least one field to update is provided
    if not any([new_id, new_bookId, new_title, new_author, new_published_date, new_quantity]):
        return jsonify({"error": "At least one update parameter (id, bookId, title, etc.) must be provided."}), 400

    # Call the `update_book` function to perform the update
    if update_book(
        id=id,
        bookId=bookId,
        title=title,
        author=author,
        published_date=published_date,
        quantity=quantity,
        new_id=new_id,
        new_bookId=new_bookId,
        new_title=new_title,
        new_author=new_author,
        new_published_date=new_published_date,
        new_quantity=new_quantity
    ):
        return jsonify({'message': 'Book updated successfully'}), 200
    else:
        return jsonify({'error': 'No books found matching the provided parameters.'}), 404


@app.route('/inventory', methods=['DELETE'])
def delete_existing_book():
    # Get query parameters from the request
    id = request.args.get('id')
    bookId = request.args.get('bookId')
    title = request.args.get('title')
    author = request.args.get('author')
    published_date = request.args.get('published_date')
    quantity = request.args.get('quantity')

    # Try to convert id, bookId, and quantity to integers if possible
    if id:
        try:
            id = int(id)
        except ValueError:
            return jsonify({"error": "'id' should be an integer."}), 400

    if bookId:
        try:
            bookId = int(bookId)
        except ValueError:
            return jsonify({"error": "'bookId' should be an integer."}), 400

    if title and not isinstance(title, str):
        return jsonify({"error": "'title' should be a string."}), 400

    if author and not isinstance(author, str):
        return jsonify({"error": "'author' should be a string."}), 400

    if published_date and not isinstance(published_date, str):
        return jsonify({"error": "'publiched_date' should be a string."}), 400

    if quantity:
        try:
            quantity = int(quantity)
        except ValueError:
            return jsonify({"error": "'quantity' should be an integer."}), 400

    # Call the function to delete the book
    if delete_book(id=id, bookId=bookId, title=title, author=author, published_date=published_date, quantity=quantity):
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
        return jsonify({'error': 'No book found matching the provided parameters'}), 404



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8083)
    # app.run(debug=True,port=8083)
