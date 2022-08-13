from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

class Grade(models.Model):
    grade = models.IntegerField(default=7)

class Group(models.Model):
    title = models.TextField(blank = True,null = True,default='name') 
    level = models.IntegerField(default=1)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='groups', null=True)

    class Meta:
        ordering = ['level', 'title', 'id']

    # def get_absolute_url(self):
    #     return reverse("accounts:profile", kwargs={"id": self.id})