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
    image = models.ImageField(upload_to='images/', null=True)
    starting_price = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    current_price = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP', null=True)
    expire_time = models.DateTimeField()
    current_bidder = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      null=True,
      related_name='current_bidder'
    )

    def __str__(self):
        return self.title

class Question(models.Model):
    question = models.CharField(max_length=300)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False)
    answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, null=True)
    answer = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
