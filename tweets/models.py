from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweets(models.Model):
    author = models.ForeignKey(User, on_delete= models.DO_NOTHING,related_name="authors")
    message = models.CharField(max_length=1000, blank= True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="likes")