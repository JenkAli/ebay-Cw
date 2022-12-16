import json
from django.shortcuts import get_object_or_404, render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse, JsonResponse
from .serializers import ItemSerializer, UpdateItemSerializer, QuestionSerializer, AnswerSerializer, UploadItemImageSerializer
from .models import Item, Question, Answer
from users.models import MyUser
from django.utils import timezone
from django.core.mail import send_mail

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
def upload_image(request, itemId):
    if request.method == 'POST':
        image = request.FILES['image']
        with open('./images/' + image.name, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)
        path="/images/"+ image.name
        print(path)
        items = Item.objects.filter(id=itemId).first()
        items.image = path
        items.save()
        return HttpResponse('Worked')
    else:
        return HttpResponse('Invalid request')
    
@csrf_exempt
def itemsByUser(request, userId):
    remove_expired_objects()
    if(request.method == 'GET'):
        items = Item.objects.filter(owner=userId)
        serializer = ItemSerializer(items, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    else: return JsonResponse({"message": "no items"})



@csrf_exempt
def updateItem(request, pk):
    remove_expired_objects()
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
def view_questions(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    questions = Question.objects.filter(item=item)
    answers = Answer.objects.filter(question__in=questions)
    question_answer_list = []
    for question in questions:
        answer = answers.filter(question=question).first()
        if answer:
            answer_text = answer.answer_text
        else:
            answer_text = ''
        question_answer_list.append({'id': question.id, 'question': question.question_text, 'answer': answer_text})
    return JsonResponse(question_answer_list, safe=False)

@csrf_exempt
def send_question(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        question_text = data.get('question_text', '')
        user = MyUser.objects.filter(id=data.get('userId')).first()
        if not question_text:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        question = Question.objects.create(item=item, question_text=question_text, sender=user, receiver=item.owner)
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data)
    
@csrf_exempt
def answer_question(request, question_id):
    questionId = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        user = MyUser.objects.filter(id=data.get('userId')).first()
        answer_message = data.get('answer_text', '')
        if not answer_message:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        answer = Answer.objects.create(question=questionId, sender=user, receiver=questionId.item.owner, answer_text=answer_message)
        serializer = AnswerSerializer(answer)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

        
@csrf_exempt
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
    
    
def remove_expired_objects():
    current_time = timezone.now()
    expired_objects = Item.objects.filter(expire_time__lt=current_time)
    email_addresses = [obj.current_bidder for obj in expired_objects]
    if expired_objects.exists():
         expired_objects.delete()
         for email_address in email_addresses:
              send_mail(
                  'YOU WON',
                  'WELL DONE YOU have won the item you bidded on',
                  'ebaycw057@gmail.com',
                  [email_address],
                  fail_silently=True,
              )
