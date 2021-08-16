from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Treasure(models.Model):
    author = models.ForeignKey(User, on_delete= models.DO_NOTHING,related_name="author_id")
    name = models.CharField(max_length=1000, unique=True)
    description = models.TextField(blank= True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15)
    latitude = models.DecimalField(max_digits=30, decimal_places=15)
    date = models.DateTimeField(auto_now_add=True)
    hunters = models.ManyToManyField(User, related_name="hunter_id", blank=True)
    