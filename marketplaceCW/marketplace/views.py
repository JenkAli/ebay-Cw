from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import ItemSerializer, UpdateItemSerializer, QuestionSerializer
from .models import Item, Question, Answer
from django.utils import timezone

# Create your views here.
@csrf_exempt
def items(request):
    remove_expired_objects()
    if(request.method == 'GET'):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def updateItem(request, pk):
    remove_expired_objects()
    try:
        result = Item.objects.get(pk=pk)
    except:
        return JsonResponse('Error', status=404)  
    if(request.method == 'PUT'):
        data = JSONParser().parse(request)  
        serializer = UpdateItemSerializer(result, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def searchItems(request):
    remove_expired_objects()
    query = request.GET.get('q')
    if query is None:
        return JsonResponse({'error': 'No search query provided'})
    items = Item.objects.filter(title__contains=query) | Item.objects.filter(description__contains=query)
    serializer = ItemSerializer(items, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False)

def remove_expired_objects():
    current_time = timezone.now()
    expired_objects = Item.objects.filter(expire_time__lt=current_time)
    expired_objects.delete()