from django.shortcuts import render, redirect, HttpResponseRedirect
from core import models 
from .models import Project, Customer, Tool


def home(request):
<<<<<<< HEAD
    diction= {}
=======
    project_list = Project.objects.all().order_by('project_name')

    diction= {'project_list':project_list}
>>>>>>> 701fc101713d193ab2796d6ad6f9f92b4d5b5e90
    return render(request, 'core/home.html', context=diction) 

def projects(request):
    project_list = Project.objects.order_by('project_name')
    diction= {'project_list':project_list}
    return render(request, 'core/projects.html', context=diction) 
  

