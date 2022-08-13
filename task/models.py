from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

from content.models import Paper
from account.models import Profile

def upload_location(instance, filename):
    TaskModel = instance.__class__
    if TaskModel.objects.order_by("id").last():
        new_id = TaskModel.objects.order_by("id").last().id + 1
    return "%s" %(filename)

class Tag(models.Model):
    title = models.TextField(blank = True,null = True,default='combinatorics')

class Task(models.Model):
    level = models.TextField(blank = True,null = True,default='name') 
    # Wood Silver Gold
    # Practice = 1 Wood
    # Easy guess = 3 Wood
    # Easy think = 7 Wood ГЖО IMC IMSO
    # Middle = 1 steel Район-1
    # Middle+ = 7 steel Район-2-3 Область-1
    # Hard = 1 gold Респа-1
    # Pro = 3 gold Респа-2 IMO-1-2
    # Impossible = 10 gold

    # Problem part
    problem = models.TextField(blank = True,null = True,default='name')
    image = models.ImageField(upload_to=upload_location, 
            null=True,
            blank=True, 
            )          

    # Solution part
    answer = models.TextField(blank = True,null = True,default='name')
    source = models.TextField(blank = True,null = True,default='name')
    hints = models.ManyToManyField(Paper, through='TaskPaperOrder')
    tags = models.ManyToManyField(Tag, related_name="tasks")

    who_solved = models.ManyToManyField(Profile, related_name='solved_problems')

    class Meta:
        ordering = ['level', 'id']

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"id": self.id})

class TaskPaperOrder(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    content = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True)
    order = models.IntegerField(default=0)
    type_of = models.CharField(default='main', max_length=10) # main secondary  