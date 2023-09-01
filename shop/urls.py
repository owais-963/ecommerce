from django.urls import path
from . import views

urlpatterns = [

    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("", views.index, name="index"),
    path("logout", views.logOut, name="logOut"),
    path("profile", views.profile, name="profile"),
    path("orders", views.orders, name="orders"),
    path("categories", views.categories, name="categories"),
    path("explore", views.explore, name="explore"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("contact", views.contact, name="contact"),
]
