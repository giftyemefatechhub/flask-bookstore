import unittest
from bookstore_assignment import app, Store, Book

class TestBookstore(unittest.TestCase):

    def setUp(self):
        self.store = Store()
        self.app = app.test_client()
        self.app.testing = True

    def test_add_book(self):
        self.store.add_book(Book(author="commander shepard", title="Normandy manual", score=0,price=0.0))
        self.assertEqual(len(self.store.books), 1)
        self.assertEqual(self.store.books["Normandy manual"].author, "commander shepard")

    def test_fillup_store(self):
        self.store.fillup_store()
        self.assertEqual(len(self.store.books), 2)

    def test_list_books_as_json(self):
        self.store.fillup_store()
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        books = response.get_json()
        self.assertEqual(len(books), 2)
        expected = {
            "author": "Stephen King",
            "title": "the long walk",
            "score": 2,
            "price": 19.99
        }
        self.assertDictEqual(books["the long walk"],expected)
    
    def test_get_single_book_by_title(self):
        self.store.fillup_store()
        response = self.app.get('/books/the martian')
        self.assertEqual(response.status_code, 200)
        book = response.get_json()
        expected = {
        "author": "Andy Weir",
        "title": "the martian",
        "score": 5,
        "price": 24.99
        }
        self.assertDictEqual(book, expected)

if __name__ == '__main__':
    unittest.main()