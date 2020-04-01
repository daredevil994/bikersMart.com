from django import forms
from postApp.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ('image','caption','date')

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=('body','name')
