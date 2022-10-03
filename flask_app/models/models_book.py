from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_author
db = 'books_authors'

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_who_favorited = []

    # Setup query to get all books
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(db).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    # Setup query to add book
    @classmethod
    def add_book(cls,data):
        query = """
                INSERT INTO books (title, num_of_pages, created_at, updated_at)
                VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW())
                """
        return connectToMySQL(db).query_db(query,data)

    # Setup query to show one author
    @classmethod
    def show_one_book(cls,data):
        query = """
                SELECT * FROM books
                WHERE id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query,data)
        return results

    # Setup query to show unfavorited books of a specific author
    @classmethod
    def unfavorited_books(cls,data):
        query = """
                SELECT * FROM books 
                WHERE books.id 
                NOT IN (SELECT book_id FROM favorites WHERE author_id = %(id)s)
                """
        results = connectToMySQL(db).query_db(query,data)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    # Setup query to retrieve the specific book along with all the authors that favorited it
    @classmethod
    def show_book_with_authors(cls,data):
        query = """
                SELECT * FROM books
                LEFT JOIN favorites ON books.id = book_id
                LEFT JOIN authors ON author_id = authors.id
                WHERE books.id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query,data)
        book = cls(results[0])
        for row_from_db in results:
            author_data = {
                "id": row_from_db["authors.id"],
                "name": row_from_db["name"],
                "created_at": row_from_db["authors.created_at"],
                "updated_at": row_from_db["authors.updated_at"]
            }
            book.authors_who_favorited.append(models_author.Author(author_data))
        return book