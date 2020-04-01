from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from signUpApp.forms import UserProfileInfoForm, SignUpForm

from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,'signUpApp/signUp.html')
def sign_up_form_view(request):
    registered= False
    if request.method == 'POST':
        user_form =SignUpForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # print("Validation Success!")
            # print("Username: " +user_form.cleaned_data['username'])
            # print("Email: " +user_form.cleaned_data['email'])
            # #print("Gender:" +form.cleaned_data['gender'])
            # # print("Age:" +form.cleaned_data['birthdate'])
            # print("Username: " +user_form.cleaned_data['username'])
            # print("Password: " +user_form.cleaned_data['password'])
            # # user =user_form.save()
            user= User.objects.create_user(username=user_form.cleaned_data['username'],
                                            email=user_form.cleaned_data['email'],
                                            password=user_form.cleaned_data['password'],
                                            first_name=user_form.cleaned_data['first_name'],
                                            last_name=user_form.cleaned_data['last_name']
                                            )
            # user.set_password(user.password) #there's is the problem i think
            user.save()
            profile= profile_form.save(commit=False)
            profile.user=user
            if 'image' in request.FILES:
                profile.image =request.FILES['image']
            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = SignUpForm()
        profile_form = UserProfileInfoForm()

    return render (request, 'signUpApp/signUp.html', context={"registered":registered, "user_form":user_form, "profile_form":profile_form })
#
#
# def sign_up_form_view(request):
#     form= forms.SignUpForm()
#     form_dict={'form':form}
#
#     if request.method== 'POST':
#         form = forms.SignUpForm(request.POST)
#
#
#
#
#     return render(request,'signUpApp/signUp.html',context=form_dict)
