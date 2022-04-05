from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from core import models
from core.form import ProjectForm 
from .models import Developer, Project, Customer, Tool
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
            return redirect('/add_project')
 
                

        diction = {'myform':myform}
        
        return render(request, 'core/home.html', context=diction)
    

  

def task(request, pk):

    tasks = Project.objects.get(id=pk).project_task.all()
    context = {
        'tasks': tasks,
    }

    return render(request, 'core/task.html', context)

def addTask(request): 
 
    if request.method == 'POST':
        d = Developer.objects.get(id=1)

        # p = Project.objects.get(id = 1)
        t = Task(task_name = 'No Task')
        t.developer.add(d)


       # 
       # t.project.add(p)
        #t.save()

    print(request.POST)

    return render(request, 'core/addtask.html')


def test(request, pk):

    return HttpResponse('hi')

