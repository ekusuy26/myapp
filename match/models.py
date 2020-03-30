from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    origin = models.ImageField(upload_to="photos/%y/%m/%d/")
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    self_introduction = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    objects = models.Manager
    dog_name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    height = models.IntegerField
    weight = models.IntegerField