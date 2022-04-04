from calendar import c
from pyexpat import model
from tkinter.tix import Tree
from unicodedata import name
from django.db import models
from django.urls import clear_script_prefix


class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    organization = models.CharField(max_length=20)


class Tools(models.Model):
    name = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=100, null=True, blank=Tree)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    tools = models.ManyToManyField(Tools, blank=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
