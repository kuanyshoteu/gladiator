from django.contrib import admin
from .models import *

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'problem', 'level']
    list_display_links = ["id"]
    search_fields = ["problem"]
    
    class Meta:
        model = Task

admin.site.register(Task, TaskModelAdmin)

class TaskPaperOrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', "order", "type_of"]
    list_display_links = ["id", 'order']
   
    class Meta:
        model = TaskPaperOrder

admin.site.register(TaskPaperOrder, TaskPaperOrderModelAdmin)