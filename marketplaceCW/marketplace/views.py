from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import ItemSerializer, UpdateItemSerializer, QuestionSerializer, AnswerSerializer
from .models import Item, Question, Answer

# Create your views here.
@csrf_exempt
def items(request):
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
    try:
        result = Item.objects.get(pk=pk)
    except:
        return JsonResponse('Error', status=404, safe=False)  
    if(request.method == 'PUT'):
        data = JSONParser().parse(request)  
        serializer = UpdateItemSerializer(result, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)
        
@csrf_exempt
def itemQuestions(request, id):
    print(request)
    try:
        result = Item.objects.get(pk=id)
    except:
        return JsonResponse('Error', status=404, safe=False) 
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)
    elif(request.method == 'GET'):
        questions = Question.objects.filter(item_id=id)
        serializer = QuestionSerializer(questions, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def allItemAnswers(request, pk):
    try:
        itemResult = Item.objects.get(pk=pk)
    except:
        return JsonResponse('Error', status=404, safe=False)
    if(request.method == 'GET'):
        answers = Answer.objects.filter(item_id=pk)
        serializer = AnswerSerializer(answers, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def itemAnswers(request, id, pk):
    try:
        itemResult = Item.objects.get(pk=id)
        questionResult = Question.objects.get(pk=pk)
    except:
        return JsonResponse('Error', status=404) 
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = AnswerSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'GET'):
        answers = Answer.objects.filter(question_id=pk, item_id=id)
        print(answers)
        serializer = AnswerSerializer(answers, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
