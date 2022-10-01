# Books-and-Authors

This project demonstrates my skill of connecting Flask to a database; use many-to-many relationships; display and create data from/into the database. 

Task: 
1. Create a new Flask project and connect to the "books_authors" database. 
2. Create a page to Add a new Author, and display all Authors from database. 
  - After create a new author, redirect to the "Authors" page.
  - On `Authors` page, Author link will redirect to `Author Show` page.
  - On `Author Show` page, create a table with all of the books the author has favorited.
  - Create a dropdown with all the books from the DB, that allows you to add a new favorite to the authors page you are on.
3. `Add Book` link will redirect to `Books` page.
  - Author drop down has a list authors in the DB.
4. After create a new book, redirect to the `Books` page.
5. On `Books` page, Book link will redirect to `Book Show` page.
  - On `Book Show` page, create a list with all of the authors that have favorited the book.
  - Create a dropdown with all the authors from the DB, that allows you to add a new author to the list of books favorite authors
6. On `Author Show` page, only display the books in the drop down that have not already been added to the authors favorites.
7. On `Book Show` page, only display the authors in the drop down that have not already been added to the list of books favorite authors.
