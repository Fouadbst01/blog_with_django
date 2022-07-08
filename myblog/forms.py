from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=55)
    last_name = forms.CharField(max_length=55)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class SaveBlgoForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title","content"]

