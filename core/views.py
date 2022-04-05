from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponseRedirect
from core import models
from core.form import ProjectForm 
from .models import Project, Customer, Tool
from core import models 
from .models import Project, Customer, Task, Tool


def home(request):
    projects = Project.objects.all()
    context= {
        'projects': projects
    }
    return render(request, 'core/home.html', context) 

def projects(request):
    project_list = Project.objects.all().order_by('project_name')
    diction= {
        'project_list':project_list
        }
    return render(request, 'core/projects.html', context=diction) 

def add_project(request):
    myform = ProjectForm()
    if request.method == 'POST':
            
        myform = ProjectForm(request.POST)
        project_name= request.POST.get('project_name')
        end_date = request.POST.get('end_date')
        tool = request.POST.get('tool')
        customer = request.POST.get('customer')
        if myform.is_valid():
            myform.save(commit=True)
 
                

        diction = {'myform':myform}
        return render(request, 'core/usersignup.html', context=diction)
    

  
def task(request, pk):

    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }

    return render(request, 'core/task.html', context)

