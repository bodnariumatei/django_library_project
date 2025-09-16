from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.logged_out, name="logout"),
    path("pending/", views.pending, name="pending"),
    path("redirecting/", views.redirecting, name="redirecting")
]