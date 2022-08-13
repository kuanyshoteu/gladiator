from django.contrib import admin
from .models import *

class LessonModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'order']
    list_display_links = ["id", 'title']
    search_fields = ["title"]
    
    class Meta:
        model = Lesson

admin.site.register(Lesson, LessonModelAdmin)

class ExerciseModelAdmin(admin.ModelAdmin):
    list_display = ['id', "order", "type_of"]
    list_display_links = ["id", 'order']
   
    class Meta:
        model = Exercise

admin.site.register(Exercise, ExerciseModelAdmin)