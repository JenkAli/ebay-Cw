from rest_framework import routers,serializers,viewsets
from .models import MyUser

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'date_of_birth']

class UpdateUserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'date_of_birth']