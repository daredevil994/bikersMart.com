from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from postApp.forms import PostForm

@login_required
def create_post(request):
    if request.method == 'POST':
        post_form= PostForm(request.POST)

        if post.is_valid() :
            post= post_form.objects.all()
        if 'image' in request.FILES:
            post.image =request.FILES['image']
        post.save()
    else:
        post_form=PostForm()

    return render(request,'myProfileApp/myProfile.html',{'post_form':post_form})
