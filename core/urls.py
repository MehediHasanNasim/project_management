from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('task/<int:pk>/', views.task, name='task'),
    path('add-task/<int:pk>/', views.addTask, name='add-task'),
    path('update-task/<int:pk>/', views.updateTask, name='update-task'),
    path('delete-task/<int:pk>/', views.deleteTask, name='delete-task'),

    path('add_project/', views.add_project, name='add_project'),
    path('project_info/<int:id>/', views.project_info, name="project_info"),
    path('project_update/<int:project_id>/', views.project_update, name="project_update"),
    path('project_delete/<int:project_id>/', views.project_delete, name="project_delete"),
    
    path('location/', views.location, name="location"),
    path('test/<int:pk>', views.test, name='test'),
]
