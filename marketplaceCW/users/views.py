from .models import MyUser
from django.http import HttpResponse, JsonResponse
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
def getAllUsers(request):
    if(request.method == 'GET'):
        users = MyUser.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        print(serializer)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def users(request, pk):
    try:
        result = MyUser.objects.get(pk=pk)
    except:
        return JsonResponse('Error', status=404)
    if(request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = UserSerializer(result, data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'GET'):
        serializer = UserSerializer(result)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def getUserByEmail(request, email):
    print(email)
    try:
        result = MyUser.objects.get(email=email)
        print(result)
    except:
        return JsonResponse('Error', status=404, safe=False)
    if(request.method == 'GET'):
        serializer = UserSerializer(result)
        return JsonResponse(serializer.data,safe=False)