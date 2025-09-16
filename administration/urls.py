from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.admin_reports, name="reports"),
    path('reports/', views.admin_reports, name="reports"),
    path('users/', views.admin_users, name="users"),
    path('users/<int:u_id>', views.admin_user, name="user"),
    path('books/', views.admin_books, name="books"),
    path('books/<int:b_id>', views.admin_update_book, name="update_book"),
    path('create_book/', views.admin_create_book, name="create_book"),
]