from django.contrib import admin
from django.shortcuts import redirect
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from operator import itemgetter

@csrf_exempt
def register(request):
     if request.method == 'POST':
        data = JSONParser().parse(request)
        email, password, date_of_birth = itemgetter('email', 'password', 'dob')(data)
        new_user = MyUser.objects._create_user(email,date_of_birth,password, image="images/placeholder.jpg")
        new_user.save()
        return HttpResponse(status=201)

# Create your views here.
@csrf_exempt
def users(request):
    if(request.method == 'GET'):
        users = MyUser.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        print(serializer)
        return HttpResponse(serializer.data)
