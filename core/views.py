from multiprocessing import context
from dateutil import parser
from datetime import timedelta
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.form import ProjectForm 
from .models import Developer, Project, Customer, Tool
from core import models 
from .models import Project, Customer, Task, Tool, TaskPriority
from . form import TaskForm, ProjectForm
from core import form
from . form import TaskForm, ProjectForm, UpdateTaskForm
from django.http import JsonResponse




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


def project_info(request, id):
    project = Project.objects.filter(pk=id)
    if project:
        project= Project.objects.get(pk=id)
    diction = {'project':project}
    print('project')
    return render (request, 'core/project_info.html', context=diction)


def project_update(request, project_id):
    project_info = Project.objects.get(pk=project_id)
    update_form = form.ProjectForm(instance=project_info)

    if request.method =="POST":
        update_form = form.ProjectForm(request.POST, instance=project_info)
        
        if update_form.is_valid():
            update_form.save(commit=True)
            return projects(request)

    diction = {'update_form': update_form}
    return render (request, 'core/project_update.html', context=diction)


def project_delete(request, project_id):
    project= Project.objects.get(pk=project_id).delete()
    diction = {'delete_message': "Delete Done"}
    return render (request, 'core/project_delete.html', context=diction)

def location(request):
    diction= {}
    return render(request, 'core/location.html', context=diction) 



def task(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        'tasks': project.task_set.all(),
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
    task_form = UpdateTaskForm(instance= task)

    context = {
        'developers': developers,
        'prioritys': prioritys,
        'task': task,
        'start_date': start_date,
        'task_form': task_form,
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
    context = {
        'project_id': project_id
    }

    if request.method == 'POST':
        task.delete()
        return redirect('task', project_id)

    return render(request, 'core/delete-task.html')

def jqGridApi(request):
   
   project = Project.objects.get(id=5)
   tasks = project.task_set.all()

   dev_name = ''
   def developerLits(dev):
       dev_name = ''
       for i in dev:
            print(i)
            dev_name +=str(i)+','
       return dev_name

   all_tasks = []

   for i in tasks:
       task = {
        "id": i.id,
       "task_name": i.task_name,
       "start_date": i.start_date,
       "end_date": i.start_date,
       "developers": developerLits(i.developer.all()),
       "priority": i.priority.priority

       }

       all_tasks.append(task)
        

   return JsonResponse(all_tasks, safe=False)


def jqGrid(request):

  
   context = {
        'tasks': '',
        'project': 'project'
    }
   return render (request, 'core/jqgrid.html', context)

def test(request, pk):

    return HttpResponse('hi')




