from django.contrib import admin
from . models import Tool, Project, Customer, Developer, Task, TaskPriority

admin.site.register(Tool)
admin.site.register(Project)
admin.site.register(Customer)
admin.site.register(Developer)
admin.site.register(Task)
admin.site.register(TaskPriority)
