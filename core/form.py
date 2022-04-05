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
        fields = ['project_name', 'start_date', 'end_date', 'tool', 'customer']



class TaskForm(forms.ModelForm):

    class  Meta:
        model = Task
        fields = '__all__'


<<<<<<< HEAD
=======
      

       
    
>>>>>>> a0422ac372a4953fa20455f57a3ae9ad5a615395



        

