# Django Library Project
Project developed to teach myself the Django Pyhton framework.
Bootstrap used to make everything look a bit better.

## Features:
  - login
  - register as new user
  - users can't acces the library pages untill an admin approves their account
  - a user can:
      * see the books in the library
      * borrow books
      * return books
      * see borrowing history and currently borrowed books
  - custom admin pages
  - reports admin page, with reports for all books in library and their availability and reports for the currently borrowed books
  - an admin can:
      * add/modify/remove books
      * search for book by title or author
      * approve user accounts
      * make users admins
      * remove users

## The Django project contains 3 apps: 
  - library - where all the library related logic takes place: listing books, borrowing, returning
  - accounts - deals with the login and register features
  - administration - custom admin pages
