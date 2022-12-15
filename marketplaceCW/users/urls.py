from django.urls import path
from .views import register, loginUser, users

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', loginUser, name="login"),
    path('users/', users, name="users"),
]