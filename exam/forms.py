from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Class, Exam, Question, Option


class CreateuserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name' ,'username', 'email', 'password1', 'password2']


class UpdateuserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name' ,'username', 'email', 'password1', 'password2']

class CreateClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'description']

