from django.urls import path
from .views import loginPage, registerPage

urlpatterns = [
    path('register', registerPage, name="register"),
    path('login', loginPage, name="login"),
]