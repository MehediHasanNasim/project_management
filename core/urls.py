from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('task/<int:pk>/', views.task, name='task'),
    path('add-task/<int:pk>/', views.addTask, name='add-task'),
    path('update-task/<int:pk>/', views.updateTask, name='update-task'),

    path('add_project/', views.add_project, name='add_project'),


    path('test/<int:pk>', views.test, name='test'),
]
