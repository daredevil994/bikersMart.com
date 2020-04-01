from django.shortcuts import render
from . import forms

from myProfileApp.views import my_profile

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'signInApp/signIn.html')

@login_required
def profile_view(request):
    return render(request,'myProfileApp/my_profile.html')

def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('myProfileApp:my_profile'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE!")
        else:
            # print("Someone Failed To Log In!")
            # print("username: {} and Password: {}".format(username,password))
            return render(request,'signInApp/signIn.html',{})
    else:
        return render(request,'signInApp/signIn.html',{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
#
# def sign_in_form_view(request):
#     form= forms.SignInForm()
#     form_dict={'form':form}
#     if request.method== 'POST':
#         form = forms.SignInForm(request.POST)
#         if form.is_valid():
#             print("Validation Success!")
#             print("Email: " +form.cleaned_data['email'])
#             print("Password: " +form.cleaned_data['password'])
#     return render(request,'signInApp/signIn.html',context=form_dict)
