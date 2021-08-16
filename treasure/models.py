from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Treasure(models.Model):
    author = models.ForeignKey(User, on_delete= models.DO_NOTHING,related_name="author_id")
    name = models.CharField(max_length=1000, unique=True)
    description = models.TextField(blank= True)
    longitude = models.PositiveIntegerField()
    latitude = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    hunters = models.ManyToManyField(User, related_name="hunter_id", blank=True)
    