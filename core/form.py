from dataclasses import field
from pyexpat import model
from django import forms
from core import models
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Project, Tool, Developer, TaskPriority, Task
from django.core import validators
from django.core.exceptions import ValidationError


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'



class TaskForm(forms.ModelForm):

    class  Meta:
        model = Task
        fields = '__all__'


      

        

