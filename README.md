# Django Library Project
Project developed to teach myself the Django Pyhton framework.

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
      * approve user accounts
      * make users admins
      * remove users

## The Django project contains 3 apps: 
  - library - where all the library related logic takes place: listing books, borrowing, returning
  - accounts - deals with the login and register features
  - administration - custom admin pages

## Extra packages nedeed:
  - crispy: $ pip install crispy-bootstrap5
     * useful info: https://medium.com/@azzouzhamza13/django-crispy-forms-bootstrap5-00a1eb3ec3c7
