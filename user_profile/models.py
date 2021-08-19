from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    friends = models.ManyToManyField(User, related_name="friend_id", blank=True)
    nickname = models.CharField(max_length= 20, blank= True)
    address = models.CharField(max_length= 20, blank= True)
    age = models.IntegerField(blank=True)
    about_me = models.CharField(max_length=1000,blank=True)
    image_src = models.CharField(max_length=1000, default="https://c.files.bbci.co.uk/16620/production/_91408619_55df76d5-2245-41c1-8031-07a4da3f313f.jpg")
    
    