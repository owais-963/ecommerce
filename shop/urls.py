from django.urls import path
from . import views

urlpatterns = [

    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("", views.index, name="index"),
    path("logout", views.logOut, name="logOut"),
]