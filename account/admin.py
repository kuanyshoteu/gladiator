from django.contrib import admin
from .models import *

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "mail", "group_title"]
    list_display_links = ["name"]
    search_fields = ["name"]

    def group_title(self, obj):
        return obj.group.title  
    class Meta:
        model = Profile

admin.site.register(Profile, ProfileModelAdmin)