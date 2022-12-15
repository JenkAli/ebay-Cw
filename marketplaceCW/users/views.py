from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer

def registerPage(request):
     form = CreateUserForm()
     if request.method == 'POST':
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        image = request.POST.get('image')
        password = request.POST.get('password')
        new_user = MyUser.objects._create_user(email,date_of_birth,password,image)
        new_user.save()
        return redirect('login')

     context = {'form': form}
     return render(request, 'accounts/register.html', context)

def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            print("User has logged in")
            return redirect('http://localhost:5173/')
        else:
            return HttpResponse('Error, user does not exist')
    
    return render(request, 'accounts/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login-page')



# Create your views here.
@csrf_exempt
def users(request):
    if(request.method == 'GET'):
        users = MyUser.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        print(serializer)
        return HttpResponse(serializer.data)
