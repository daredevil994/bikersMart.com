from django.db import models
from galleryApp.models import Bike, Brand

from django.contrib.auth.models import User
# from signUpApp.models import UserProfileInfo

import datetime
# from django.conf import settings
# Create your models here.


class UserProfile(models.Model):
    # user= models.OneToOneField(settings.AUTH_USER_MODEL)
    sex=(('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
        )
    marital_choices=(('Single','Single'),
                    ('Maried','Maried'),
                    ('Divorced','Divorced'),
                    ('Separated','Separated'),
                    ('In A Relationship','In A Relationship'),
                    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    image= models.ImageField(default='default.jpg',upload_to='../media/profile_pics')
    birthdate= models.DateField(null=True)
    # age=models.IntegerField(null=True)
    # def __str__(self):
    #     today= date.today()
    #     age= today.year - birthdate.year
    #     if today.month < birthdate.month or today.month == birthdate.month and today.day < birthdate.day :
    #         age -= 1
    #         return self.age

    gender= models.CharField(max_length=10,choices=sex,null=True)
    marital_status=models.CharField(max_length=18,choices=marital_choices,null=True)
    address= models.CharField(max_length=200,null=True)
    bio=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.user)

    # def create_user_profile(sender,instance,created,**kwargs):
    #     if created:
    #         UserProfile.objects.create(user=instance)
    #         post_save.connect(create_user_profile,sender=User)
class MyBike(models.Model):

    owner=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    model=models.ForeignKey(Bike,on_delete=models.CASCADE,null=True)
    distance= models.IntegerField()
    mileage= models.IntegerField()
    details= models.CharField(max_length=200,null=True)
    numberplate= models.CharField(max_length=100,null=True)
