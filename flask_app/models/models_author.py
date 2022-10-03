from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_book
db = 'books_authors'

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    # Setup query to get all authors
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(db).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
        
    # Setup query to add author
    @classmethod
    def add_author(cls,data):
        query = """
                INSERT INTO authors (name, created_at, updated_at)
                VALUES (%(name)s, NOW(), NOW());
                """
        return connectToMySQL(db).query_db(query,data)
    
    # Setup query to show one author
    @classmethod
    def show_one_author(cls,data):
        query = """
                SELECT * FROM authors
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query,data)

    # Setup query to add books and authors to the favorites table
    @classmethod
    def add_favorite(cls,data):
        query = """
                INSERT INTO favorites (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s);
                """
        return connectToMySQL(db).query_db(query,data)

    # Setup query to show unfavorited authors of a specific book
    @classmethod
    def unfavorited_author(cls,data):
        query = """
                SELECT * FROM authors 
                WHERE authors.id 
                NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s)
                """
        results = connectToMySQL(db).query_db(query,data)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    # Setup query to retrieve the specific author along with all the books that they favorited
    @classmethod
    def show_author_with_books(cls,data):
        query = """
                SELECT * FROM authors
                LEFT JOIN favorites ON authors.id = author_id
                LEFT JOIN books ON book_id = books.id
                WHERE authors.id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query,data)
        author = cls(results[0])
        for row_from_db in results:
            book_data = {
                "id": row_from_db["books.id"],
                "title": row_from_db["title"],
                "num_of_pages": row_from_db["num_of_pages"],
                "created_at": row_from_db["books.created_at"],
                "updated_at": row_from_db["books.updated_at"]
            }
            author.favorite_books.append(models_book.Book(book_data))
        return author