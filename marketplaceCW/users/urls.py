from django.urls import path
from .views import registerPage, Login, getAllUsers, users

urlpatterns = [
    path('register/', registerPage, name="registerPage"),
    path('login/', Login, name="login"),
    path('users/', getAllUsers, name="allUsers"),
    path('users/<int:pk>/', users, name="users"),
]