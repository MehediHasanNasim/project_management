from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from core import models
from core.form import ProjectForm 
from .models import Developer, Project, Customer, Tool
from core import models 
from .models import Project, Customer, Task, Tool, TaskPriority
from . form import TaskForm


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


def test(request, pk):

    return HttpResponse('hi')







#  'task_name': [''], 'start_date': [''], 'end_date': [''], 'actualTime': [''], 'project': [''], 'priority': ['']
#     if request.method == 'POST':


#  'task_name': [''], 'start_date': [''], 'end_date': ['']}>