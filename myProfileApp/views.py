from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from myProfileApp.models import UserProfile
from django.http import HttpResponse
from myProfileApp.forms import UpdateUserProfileForm, UpdateUserProfileInfoForm
from django.contrib.auth.models import User
# from signUpApp.models import UserProfileInfo
# Create your views here.\

@login_required
def my_profile(request):

    user= User.objects.get(username=request.user)
    profile=UserProfile.objects.get(user=user.id)
    profile_dict={'first_name': user.first_name,
                    'last_name':user.last_name,
                    'username':user.username,
                    'email':user.email,
                    'gender':profile.gender,
                    'birthdate':profile.birthdate,
                    'marital_status':profile.marital_status,
                    'address':profile.address,
                    'bio':profile.bio,
                    'image':profile.image
                    }
    context={'profile':profile_dict}
    # my_dict ={'name': 'daredevil994', 'age':'23', 'bike_model':'Yamaha Fazer v2 FI', 'run': '12000', }
    return render(request,'myProfileApp/myProfile.html',context)

@login_required
def settings_view(request):
    user=User.objects.get(username=request.user)
    profile=UserProfile.objects.get(user=user.id)

    # profile_dict={'image':profile.image}
    if request.method == 'POST':
        update_user=UpdateUserProfileForm(data=request.POST,instance=user)
        update_profile=UpdateUserProfileInfoForm(data=request.POST,files=request.FILES,instance=profile)
        if update_user.is_valid() and update_profile.is_valid():
            update_user.save()
            update_user.user.save()
            update_profile.save()
            update_profile.profile.save()
            # return redirect('profile')
        else:
            print(update_user.errors,update_profile.errors)
    else:
        update_user=UpdateUserProfileForm(instance=user)
        update_profile=UpdateUserProfileInfoForm(instance=profile)

    context={'update_user':update_user,
            'update_profile':update_profile,
            # 'profile_dict':profile_dict,
            }

    return render(request,'myProfileApp/updateProfile.html',context)
