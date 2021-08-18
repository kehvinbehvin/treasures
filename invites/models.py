from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# choices
CHOICES = (("NULL","NULL"),("PENDING","PENDING"), ("ACCEPT","ACCEPT"), ("DECLINE","DECLINE"))


class Invites(models.Model):
    inviter = models.ForeignKey(User, on_delete= models.DO_NOTHING, related_name='inviter_id')
    invitee = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name= 'invitee_id')
    status = models.CharField(max_length=300, choices= CHOICES, default= "NULL")

