from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Treasure(models.Model):
    author = models.ForeignKey(User, on_delete= models.DO_NOTHING,related_name="author_id")
    name = models.CharField(max_length=1000, unique=True)
    description = models.TextField(blank= True)
    lng = models.DecimalField(max_digits=30, decimal_places=15)
    lat = models.DecimalField(max_digits=30, decimal_places=15)
    date = models.DateTimeField(auto_now_add=True)
    hunters = models.ManyToManyField(User, related_name="hunter_id", blank=True)
    quiz = models.TextField(blank=True)
    mcq1 = models.CharField(max_length=1000)
    mcq2 = models.CharField(max_length=1000)
    mcq3 = models.CharField(max_length=1000)
    hint = models.TextField(blank=True)
    answer = models.TextField(blank=True)