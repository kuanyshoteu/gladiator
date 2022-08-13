import imp
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

from content.models import Paper
from task.models import Task

def upload_location(instance, filename):
    LessonModel = instance.__class__
    if LessonModel.objects.order_by("id").last():
        new_id = LessonModel.objects.order_by("id").last().id + 1
    return "%s" %(filename)
 
class Lesson(models.Model):
    title = models.TextField(blank = True,null = True,default='name')
    order = models.IntegerField(default=0)
    logo_image = models.ImageField(upload_to=upload_location, 
            null=True,
            blank=True, 
            )
    main_image = models.ImageField(upload_to=upload_location, 
            null=True,
            blank=True, 
            )

    class Meta:
        ordering = ['order', 'id']

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"id": self.id})

class Exercise(models.Model):
    order = models.IntegerField(default=0)
    logo_image = models.ImageField(upload_to=upload_location, 
            null=True,
            blank=True, 
            )
    type_of = models.CharField(default='theory', max_length=10) # theory task    
    theory = models.ManyToManyField(Paper, through='ExercisePaperOrder')
    # One exercise has several lemmas (lemma = group of contents) linked to itself
    # ExerciseContentOrder manages the order of content

    task = models.ForeignKey(Task, related_name='exercises', null=True,  on_delete=models.CASCADE)
    # One Exercise has only one task, 
    # so that we don't have to manage order of tasks in one exercise
    # Order of exercises manages order of tasks in Lesson
    class Meta:
        ordering = ['order', 'id']

    # def get_absolute_url(self):
    #     return reverse("lesson:exercise", kwargs={"id": self.id})

class ExercisePaperOrder(models.Model):
    lemma = models.ForeignKey(Paper, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    type_of = models.CharField(default='main', max_length=10) # main secondary   