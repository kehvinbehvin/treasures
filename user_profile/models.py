from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    friends = models.ManyToManyField(User, related_name="friend_id", blank=True)
    nickname = models.CharField(max_length= 20, blank= True)
    address = models.CharField(max_length= 20, blank= True)
    age = models.IntegerField()
    about_me = models.CharField(max_length=1000)
    
    