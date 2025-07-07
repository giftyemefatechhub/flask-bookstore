# Installation

# Install python: https://www.python.org/about/gettingstarted/
# Install required packages: pip install -r requirements.txt
# to run the code: python bookstore_assignment.py
# to run the tests: python -m unittest bookstore_assignment_test.py

from flask import Flask, jsonify

app = Flask(__name__)

class Book:
    def __init__(self, author, title, score, price ):
        self.author = author
        self.title = title
        self.score = score
        self.price = float(price)

class Store:
    def __init__(self):
        self.books = {}

    def fillup_store(self):
        book1 = Book(author="Stephen King", title="the long walk", score=2,
        price=19.99)
        book2 = Book(author="Andy Weir",
        title="the martian",score=5,
        price=24.99)
        self.add_book(book1)
        self.add_book(book2)

    def add_book(self, book):
        self.books[book.title] = book

    def list_books_as_json(self):
        books_dict = {title: book.__dict__ for title, book in self.books.items()}
        return jsonify(books_dict)
    
    def get_book_by_title_as_json(self, title):
        book = self.books.get(title)
        if book:
            return jsonify(book.__dict__)
        else:
            return jsonify({"error": "Book not found"}), 404

store = Store()
store.fillup_store()

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message":"Welcome to the Bookstore API",
        "endpoints":{
            "/books": "Get all books",
            "/books/:title": "Get a single book by title"
        }
    })

@app.route('/books', methods=['GET'])
def list_books():
    return store.list_books_as_json()

@app.route('/books/<title>', methods=['GET'])
def get_book_by_title(title):
    return store.get_book_by_title_as_json(title)
if __name__ == '__main__':
    app.run(port=3000)