from django.urls import path
from .views import register, users, getUserByEmail

urlpatterns = [
    path('register/', register, name="register"),
    path('users/<int:pk>', users, name="users"),
    path('users/email/<str:email>', getUserByEmail, name="userByEmail"),
]