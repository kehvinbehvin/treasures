from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    friends = models.ManyToManyField(User, related_name="friend_id", blank=True)
    nickname = models.CharField(max_length= 20, default="Null")
    address = models.CharField(max_length= 20, default="Null")
    age = models.IntegerField(blank=True, null=True)
    about_me = models.CharField(max_length=1000, default="Null")
    image_src = models.CharField(max_length=1000)
    
    