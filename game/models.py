from distutils.command.build import build
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

from account.models import Profile
from group.models import Group

def upload_location(instance, filename):
    GroupModel = instance.__class__
    if GroupModel.objects.order_by("id").last():
        new_id = GroupModel.objects.order_by("id").last().id + 1
    return "%s" %(filename)

class Map(models.Model):
    title = models.TextField(blank = True, null = True, default='earth')
    # earth mars etc.
    map_array = ArrayField(models.IntegerField(), default = list)

class Game(models.Model):    
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='games', null=True)
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='games', null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)

class Cell(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cells', null=True)
    building = models.TextField(blank = True,null = True,default='land') 
    # land, tower, castle, water, boat
    order = models.IntegerField(default=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='cells', null=True)
    class Meta:
        ordering = ['game', 'order', 'owner']

    # def get_absolute_url(self):
    #     return reverse("accounts:profile", kwargs={"id": self.id})