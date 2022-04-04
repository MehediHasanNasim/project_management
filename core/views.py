from django.shortcuts import render, redirect, HttpResponseRedirect
from core import models 
from .models import Project, Customer, Tool


def home(request):
    diction= {}
    return render(request, 'core/home.html', context=diction) 

def projects(request):
    project_list = Project.objects.all().order_by('project_name')
    diction= {'project_list':project_list}
    return render(request, 'core/projects.html', context=diction) 
  

