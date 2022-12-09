from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from .models import MyUser
admin.site.register(MyUser)

# class UserCreationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

#     class Meta:
#         model = MyUser
#         fields = ('email', 'date_of_birth', 'image')
    
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user

# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = MyUser
#         fields = ('email', 'password', 'date_of_birth', 'image')

#class UserAdmin(BaseUserAdmin):
     #form = UserChangeForm
     #add_form: UserCreationForm
     #list_display: ('email', 'date_of_birth', 'image')

#admin.site.register(MyUser, UserAdmin)

# admin.site.unregister(Group)

#Hash the above two lines out if testing as will not work atm