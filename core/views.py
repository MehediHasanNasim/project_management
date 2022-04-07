from urllib import response
from dateutil import parser
from datetime import timedelta, datetime
from pyexpat.errors import messages
from django import http
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from core import models
from core.form import ProjectForm 
from .models import Developer, Project, Customer, Tool
from core import models 
from .models import Project, Customer, Task, Tool, TaskPriority
from . form import TaskForm, ProjectForm, UpdateTaskForm


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
    
    tools = Tool.objects.all() 
    customers = Customer.objects.all() 
    myform = ProjectForm()    
    diction = {
        'myform':myform,
        'tools':tools,
        'customers': customers
    
    }


    if request.method == 'POST':
        print(request.POST)
        myform = ProjectForm(request.POST)
        

        if myform.is_valid():
            myform.save(commit=True)
            print('Project Created')
            return redirect('projects')
        else:
            print('Oops.. Try again')
 
 
    return render(request, 'core/add_project.html', context=diction)


def task(request, pk):


    project = Project.objects.get(id=pk)

    context = {
        'tasks': project.project_task.all(),
        'project': project

    }

    return render(request, 'core/task.html', context)

def addTask(request, pk): 
    developers =  Developer.objects.all()
    prioritys = TaskPriority.objects.all()
    project = Project.objects.get(id=pk)

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
            return redirect('task', pk=pk)
        else:
            print('failed')

    return render(request, 'core/addtask.html', context)


def updateTask(request, pk):

    developers =  Developer.objects.all()
    prioritys = TaskPriority.objects.all()
    task = Task.objects.get(id=pk)
    project_id = task.project.id
    
    start_date = parser.parse(str(task.start_date + timedelta(hours=6))).strftime('%Y-%m-%dT%H:%M')
    print(start_date)

    context = {
        'developers': developers,
        'prioritys': prioritys,
        'task': task,
        'start_date': start_date
    }

    if request.method == 'POST':
        print(request.POST)
        task_form = UpdateTaskForm(request.POST, instance= task)
        if task_form.is_valid():
            task_form.save(commit=True)
            return redirect('task', pk=project_id)
        else:
            print('failed')
    return  render(request, 'core/update-task.html', context)


def deleteTask(request, pk):

    task = Task.objects.get(id=pk)
    project_id = task.project.id

    print(project_id)

    context = {
        'project_id': project_id
    }

    if request.method == 'POST':
        task.delete()

        return redirect('task', project_id)


    return render(request, 'core/delete-task.html')


def test(request, pk):

    return HttpResponse('hi')




