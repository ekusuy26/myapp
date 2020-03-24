from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Image(models.Model):
   id = models.IntegerField(primary_key=True)
   objects = models.Manager
   origin = models.ImageField(upload_to="photos/%y/%m/%d/")
# Create your models here.

class UserInfo(models.Model):
    image = models.OneToOneField(Image, on_delete=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    self_introduction = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    objects = models.Manager