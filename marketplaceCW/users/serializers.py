from rest_framework import routers,serializers,viewsets
from .models import MyUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'date_of_birth', 'password', 'is_active', 'is_superuser', 'is_staff']