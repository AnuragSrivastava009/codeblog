from django.db import models

from django import forms
from django.contrib.auth.models import User
from django.conf import settings
import datetime as dt
from tinymce.models import HTMLField
from tinymce import models as tinymce_models
# Create your models here.
class login(models.Model):

    username= models.CharField(max_length=20)
    password= models.CharField(max_length=10)
    def __str__(self):
        return self.username

class register(models.Model):

    username= models.CharField(max_length=20,default=True)
    password= models.CharField(max_length=10)
    confirmpassword= models.CharField(max_length=10)
    def __str__(self):
        return self.username



class contact(models.Model):
    nam= models.CharField(max_length=122, default=True)
    email = models.EmailField(max_length=122)
    phoneno= models.CharField(max_length=12)
    message = models.CharField(max_length=122)
    def __str__(self):
        return self.email



class item(models.Model):
    title =models.CharField(max_length=100)
    img = models.ImageField(blank=True)
    


    def __str__(self):
        return self.title

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=100)
    tutorial_content = tinymce_models.HTMLField()
    title = models.ForeignKey(item, default=1, on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=120, default=1)
    tutorial_published = models.DateTimeField('date published', default=dt.datetime.now)

    def __str__(self):
        return self.tutorial_title

