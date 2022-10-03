from flask_app import app
from flask import request, render_template, redirect
from flask_app.models import models_author
from flask_app.models import models_book

@app.route('/authors')
def authors():
    authors = models_author.Author.get_all_authors()
    return render_template('/authors.html', authors=authors)

# Add author
@app.route('/add_author', methods=['POST'])
def add_author():
    models_author.Author.add_author(request.form)
    return redirect('/authors')

# Show author and author's favorite books
@app.route('/authors/<int:author_id>')
def show_author(author_id):
    data = {
        "id": author_id
    }
    author = models_author.Author.show_author_with_books(data)
    unfavorited_books = models_book.Book.unfavorited_books(data)
    return render_template('/author_show.html', author=author, unfavorited_books=unfavorited_books)

# Add book to author's favorite
@app.route('/add_fav_book', methods=['POST'])
def add_fav_book():
    models_author.Author.add_favorite(request.form)
    author_id = request.form['author_id']
    print(author_id)
    return redirect(f'/authors/{author_id}')