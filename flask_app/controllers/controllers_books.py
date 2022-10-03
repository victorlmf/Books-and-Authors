from flask_app import app
from flask import request, render_template, redirect
from flask_app.models import models_author
from flask_app.models import models_book

@app.route('/books')
def books():
    books = models_book.Book.get_all_books()
    return render_template('/books.html',books=books)

# Add book
@app.route('/add_book', methods=['POST'])
def add_book():
    models_book.Book.add_book(request.form)
    return redirect('/books')

# Show book and authors that favorited the book
@app.route('/books/<int:book_id>')
def show_book(book_id):
    data = {
        "id": book_id
    }
    book = models_book.Book.show_book_with_authors(data)
    unfavorited_authors = models_author.Author.unfavorited_author(data)
    return render_template('/book_show.html', book=book, unfavorited_authors=unfavorited_authors)

# Add author that favorited the specific book
@app.route('/add_fav_author', methods=['POST'])
def add_fav_author():
    models_author.Author.add_favorite(request.form)
    book_id = request.form['book_id']
    return redirect(f'/books/{book_id}')
