from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse

def upload_location(instance, filename):
    ContentModel = instance.__class__
    if ContentModel.objects.order_by("id").last():
        new_id = ContentModel.objects.order_by("id").last().id + 1
    return "%s" %(filename)

class Paper(models.Model):
    # Connected group of contents
    # Could be in a theory (as part of the page)
    # Could be in a task solution (as a hint)
    # Has two options regulated by "through" classes: 
    #   1) main: regular group of contents 
    #   2) secondary (reminder of older theorems): 
    #       user see only clickable title of paper,
    #       body of the paper could be shown highlighted only after click
    # It could be in a landing page 
    title = models.TextField(blank = True,null = True,default='Untitled lemma')
    class Meta:
        ordering = ['id']

class Content(models.Model): 
    # Any piece of content (text or img) are saved here
    # It could be in theory as several contents grouped as lemmas
    # It could be in solution of task as a hint
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_location, 
            null=True,
            blank=True, 
            )
    type_of = models.CharField(default='text', max_length=10) # text img             
    text = models.TextField(blank = True,null = True,default='name')
    paper = models.ForeignKey(Paper, related_name='contents', on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ['order', 'id']

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"id": self.id})

