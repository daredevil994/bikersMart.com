from django import forms
from django.core import validators

class SignInForm(forms.Form):
    email= forms.CharField(max_length=100)
    password = forms.CharField(max_length=32)
    
