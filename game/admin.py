from django.contrib import admin
from .models import *


class CellModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'game_group', 'game_datetime', "order", "owner_name", "building"]
    list_display_links = ["id", 'game_group']
    search_fields = ["game_group"]
    def game_datetime(self, obj):
        return obj.game.datetime  
    def game_group(self, obj):
        return obj.game.group.title  
    def owner_name(self, obj):
        return obj.owner.name          
    class Meta:
        model = Cell

admin.site.register(Cell, CellModelAdmin)

class GameModelAdmin(admin.ModelAdmin):
    list_display = ['id', "datetime", "group_title", "map_title"]
    list_display_links = ["id", 'datetime']
    search_fields = ["group_title"]
    def group_title(self, obj):
        return obj.group.title    
    def map_title(self, obj):
        return obj.map.title    
    class Meta:
        model = Game

admin.site.register(Game, GameModelAdmin)

class MapModelAdmin(admin.ModelAdmin):
    list_display = ['id', "title"]
    list_display_links = ["id", 'title']
    search_fields = ["title"]

    class Meta:
        model = Map

admin.site.register(Map, MapModelAdmin)