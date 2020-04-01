from django.db import models
# from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='post_pics',null=False)
    caption= models.CharField(max_length=200, null=True)
    date= models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=60, null=True, default='annonymous')
    body= models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.name)
