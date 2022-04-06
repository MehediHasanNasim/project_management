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


def addTask(request): 

   
    developers =  Developer.objects.all()
    prioritys = TaskPriority.objects.all()
    project = Project.objects.get(id=1)

    context = {
        'developers': developers,
        'prioritys': prioritys,
        'project': project,
        'form': TaskForm()
    }

 
    if request.method == 'POST':

        print(request.POST)
        taskForm = TaskForm(request.POST)
        
        if taskForm.is_valid():
            taskForm.save(commit=True)
            print('success')
        else:
            print('failed')
 



        

