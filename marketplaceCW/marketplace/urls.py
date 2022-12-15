from django.urls import path 
from marketplace import views

# define the urls
urlpatterns = [
    path('items/', views.items, name='items'),
    path('items/<int:pk>/', views.updateItem, name='bid'),
    path('items/<int:id>/questions/', views.itemQuestions,  name='questions'),
    path('items/<int:id>/questions/<int:pk>/', views.itemAnswers, name='answers'),
    path('items/<int:pk>/answers/', views.allItemAnswers, name='allAnswers'),
]