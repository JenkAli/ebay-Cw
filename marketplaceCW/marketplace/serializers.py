from rest_framework import routers,serializers,viewsets
from .models import Item, Question, Answer

class ItemSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'owner', 'image', 'starting_price', 'current_price', 'expire_time', 'current_bidder']

class UpdateItemSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Item
        fields = ['current_price', 'current_bidder']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'item', 'user']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'item', 'answer', 'user']
