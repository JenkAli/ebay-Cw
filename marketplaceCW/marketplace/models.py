from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      null=False,
      related_name='owner'
    )
    image = models.CharField(max_length=100, blank=True, null=True)
    starting_price = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    current_price = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP', null=True)
    expire_time = models.DateTimeField()
    current_bidder = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      null=True,
      related_name='current_bidder'
    )

        
class Question(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')
    question_text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answer_sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answer_receiver')
    answer_text = models.TextField()