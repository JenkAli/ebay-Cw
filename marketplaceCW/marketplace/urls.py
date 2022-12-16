from django.urls import path 
from marketplace import views

# define the urls
urlpatterns = [
    path('items/', views.items, name='items'),
    path('items/<int:pk>/', views.updateItem),
    path('items/user/<int:userId>/', views.itemsByUser, name='itemsbyUser'),
    path('items/<int:pk>/', views.updateItem, name='bid'),
    path('items/<int:item_id>/questions/', views.view_questions,  name='questions'),
    path('items/<int:item_id>/sendquestion/', views.send_question,  name='sendquestion'),
    path('items/<int:question_id>/answer/', views.answer_question,  name='answerquestion'),
]