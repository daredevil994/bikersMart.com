from django import forms
from django.core import validators
from django.contrib.auth.models import User
# from signUpApp.models import UserProfileInfo
# import bithday
from myProfileApp.models import UserProfile

class SignUpForm(forms.ModelForm):
    # birthdate=birthday.fields.BirthdayField(required=True)
    password= forms.CharField(widget=forms.PasswordInput)

    botcatcher = forms.CharField(required=False, widget= forms.HiddenInput, validators= [validators.MaxLengthValidator(0)])

    class Meta():
        model= User
        fields=('first_name','last_name','username','email')


class UserProfileInfoForm(forms.ModelForm):

    
    class Meta():
        model=UserProfile
        fields=('image','birthdate','gender','marital_status','address','bio')
