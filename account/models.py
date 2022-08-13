from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

from group.models import Group

def upload_location(instance, filename):
    ProfileModel = instance.__class__
    if ProfileModel.objects.order_by("id").last():
        new_id = ProfileModel.objects.order_by("id").last().id + 1
    return "%s" %(filename)
 

class Profile(models.Model):
    # Client data
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    name = models.TextField(blank = True,null = True,default='name')
    mail = models.TextField(blank = True,default = '',null = True)
    birthday = models.DateField(blank=True, null = True, default = '')
    image = models.ImageField(upload_to=upload_location, 
            null=True,
            blank=True, 
            )

    # Game stuff    
    color = models.CharField(default='blue', max_length=250)
    coins = ArrayField(models.IntegerField(), default = list) # [wood, steel, bronze, silver, gold]
    sum_of_coins = models.IntegerField(default=0)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='profiles', null=True)

    # Password stuff
    confirmed = models.BooleanField(default=True)
    confirmation_code = models.CharField(default='', max_length=250)
    confirmation_time = models.DateTimeField(auto_now_add=False, default=datetime.datetime.strptime('2000-01-01', "%Y-%m-%d"))

    class Meta:
        ordering = ['sum_of_coins', '-birthday', 'id']

    def get_absolute_url(self):
        self.user.username = self.user.username.replace(' ', '_')
        self.user.username = self.user.username.replace('Қ', 'К')
        self.user.username = self.user.username.replace('қ', 'к')
        return reverse("accounts:profile", kwargs={"user": self.user})
