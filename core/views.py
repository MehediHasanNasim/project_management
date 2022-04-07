from multiprocessing import context
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from core import models
from core.form import ProjectForm 
from .models import Developer, Project, Customer, Tool
from core import models 
from .models import Project, Customer, Task, Tool, TaskPriority
from . form import TaskForm, ProjectForm
from core import form


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






def task(request, pk):


    tasks = Project.objects.get(id=pk).project_task.all()
    context = {
        'tasks': tasks,
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
            return redirect('home')
        else:
            print('failed')



        # request.POST['task_name'] = 'aabc'
        # task_name = request.POST.get('task_name')
        # start_date = request.POST.get('start_date')
        # end_date = request.POST.get('end_date')
        # actualTime = request.POST.get('actualTime')
        # developer = request.POST.get('developer')
        # #project = request.POST.get('project')
        # priority = request.POST.get('priority')
        # end_date = request.POST.get('end_date')

        # devs = Developer.objects.filter(id__in = developer)
        # priority = TaskPriority.objects.get(id=priority)

        # t = Task(task_name = task_name, start_date=start_date, end_date = end_date, actualTime=actualTime, priority=priority, project=project)    
        # t.save()
        # for i in devs:
        #     t.developer.add(i)

    return render(request, 'core/addtask.html', context)


def updateTask(request, pk):

    developers =  Developer.objects.all()
    prioritys = TaskPriority.objects.all()
    project = Project.objects.get(id=pk)

    context = {
        'developers': developers,
        'prioritys': prioritys,
        'project': project,
        'form': TaskForm()
    }


    return  render(request, 'core/update-task.html', context)


def test(request, pk):

    return HttpResponse('hi')







#  'task_name': [''], 'start_date': [''], 'end_date': [''], 'actualTime': [''], 'project': [''], 'priority': ['']
#     if request.method == 'POST':


#  'task_name': [''], 'start_date': [''], 'end_date': ['']}>