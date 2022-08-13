from django.contrib import admin
from .models import *

class ContentModelAdmin(admin.ModelAdmin):
    list_display = ['id', "type_of", "text", "order", 'paper_title']
    list_display_links = ["id", 'type_of']
    search_fields = ["text"]

    def paper_title(self, obj):
        return obj.paper.title    
    class Meta:
        model = Content

admin.site.register(Content, ContentModelAdmin)