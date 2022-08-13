from django.contrib import admin
from .models import *


class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'level', "grade_grade"]
    list_display_links = ["id", 'title']
    search_fields = ["title"]
    
    def grade_grade(self, obj):
        return obj.grade.grade  
    class Meta:
        model = Group

admin.site.register(Group, GroupModelAdmin)

class GradeModelAdmin(admin.ModelAdmin):
    list_display = ['id', "grade"]
    list_display_links = ["id", 'grade']
    search_fields = ["grade"]
    list_filter = ["grade"]
   
    class Meta:
        model = Grade

admin.site.register(Grade, GradeModelAdmin)