from flask import Flask, jsonify

app = Flask(__name__)

# Sample list of books as a list of dictionaries
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
]

# Route for the home page
@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Book API!'

# Route to get the list of books
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
