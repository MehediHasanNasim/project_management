from django.shortcuts import render, redirect, HttpResponseRedirect
from core import models 
from .models import Project, Customer, Tools 


def home(request):
    project_list = Project.objects.order_by('project_name')
    diction= {'project_list':project_list}
    return render(request, 'core/home.html', context=diction) 


