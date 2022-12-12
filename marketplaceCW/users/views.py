from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import UserSerializer
from .models import MyUser

# Create your views here.
@csrf_exempt
def users(request):
    if(request.method == 'GET'):
        users = MyUser.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        print(serializer)
        return HttpResponse(serializer.data)