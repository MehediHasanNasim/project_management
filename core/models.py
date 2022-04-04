from django.db import models

class Customer(models.Model):
    name =               models.CharField(max_length=20)
    email =              models.EmailField()
    phone =              models.IntegerField()
    organization =       models.CharField(max_length=20)
    

