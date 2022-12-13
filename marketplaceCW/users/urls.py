from django.urls import path
from .views import registerPage, Login

urlpatterns = [
    path('register/', registerPage, name="registerPage"),
    path('login/', Login, name="login")
]