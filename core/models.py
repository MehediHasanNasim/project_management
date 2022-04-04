from calendar import c
from pyexpat import model
from tkinter.tix import Tree
from unicodedata import name
from django.db import models
from django.urls import clear_script_prefix


class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=32)
    organization = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name


class Tool(models.Model):
    tool_name = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.tool_name


class Project(models.Model):

    
    project_name = models.CharField(max_length=100, null=True, blank=Tree)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    tool = models.ManyToManyField(Tool, blank=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name




class Developer(models.Model):
    devoloper_name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.devoloper_name

class TaskPriority(models.Model):
    priority = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.priority


class Task(models.Model):
    task_name = models.CharField(max_length=128, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    actualTime = models.DateField(null=True, blank=True)
    developer = models.ManyToManyField(Developer, blank=True)
    priority = models.ForeignKey(TaskPriority, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.task_name









    



