from django import forms
# from django.core import validators
from django.contrib.auth.models import User
from myProfileApp.models import UserProfile

class UpdateUserProfileForm(forms.ModelForm):

    class Meta():
        model= User
        fields=('first_name','last_name','username')


class UpdateUserProfileInfoForm(forms.ModelForm):


    class Meta():
        model=UserProfile
        fields=('image','birthdate','gender','marital_status','address','bio')
