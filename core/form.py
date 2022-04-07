from django import forms
from .models import Project,Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'start_date', 'end_date', 'tool', 'customer']



class TaskForm(forms.ModelForm):
    class  Meta:
        model = Task
        fields = '__all__'

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [ 'start_date', 'end_date', 'actual_hour']





