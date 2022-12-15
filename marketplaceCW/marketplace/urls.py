from django.urls import path 
from marketplace import views

# define the urls
urlpatterns = [
    path('items/', views.items, name='items'),
    path('items/<int:pk>/', views.updateItem),
    path('items', views.searchItems, name='searchItems')
    #path('items/<int:id>/questions/', views.itemQuestions)
]