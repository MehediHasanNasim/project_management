from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('task/<int:pk>/', views.task, name='task'),
    path('add-task/', views.addTask, name='add-task'),


    path('test/<int:pk>', views.test, name='test'),
]
