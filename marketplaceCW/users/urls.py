from django.urls import path 
from users import views

# define the urls
urlpatterns = [
    path('users/', views.users),
]