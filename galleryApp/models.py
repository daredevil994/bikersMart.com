from django.db import models

# Create your models here.

class Showroom(models.Model):
    company_name=models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.company_name

class Brand(models.Model):
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=60, unique=True)


    def __str__(self):
        return self.brand_name

class Bike(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    model = models.CharField(max_length=60)
    price= models.IntegerField()
    color=models.CharField(max_length=60)
    cc= models.IntegerField()

    def __str__(self):
        return self.model
