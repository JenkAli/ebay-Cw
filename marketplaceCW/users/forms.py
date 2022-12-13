from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class CreateUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['email', 'date_of_birth', 'image']