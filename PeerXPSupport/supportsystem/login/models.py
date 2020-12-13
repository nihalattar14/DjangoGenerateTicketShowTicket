from django.db import models

# Create your models here.

class User1(models.Model):
    id = models.AutoField(primary_key = True)
    first_name =models.CharField(max_length=30)
    last_name =models.CharField(max_length=30)
    email =models.CharField(max_length=30)
    password =models.CharField(max_length=30)

# class support(models.Model):
#     id = models.AutoField(primary_key = True)
#     department =models.CharField(max_length=50)
#     category =models.CharField(max_length=30)
#     subject =models.CharField(max_length=30)
#     description =models.CharField(max_length=30)
#     contact_name =models.CharField(max_length=30)
#     email =models.CharField(max_length=30)
#     phone =models.CharField(max_length=30)
#     priority =models.CharField(max_length=30)
#     attach =models.CharField(max_length=30)
