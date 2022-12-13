from django.urls import path
from .views import registerPage, Login, users

urlpatterns = [
    path('register/', registerPage, name="registerPage"),
    path('login/', Login, name="login"),
    path('users/', users, name="users"),
]