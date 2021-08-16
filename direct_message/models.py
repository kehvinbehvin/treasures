from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Direct(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender_id'
)
    recipient = models.ForeignKey(User, on_delete=models.DO_NOTHING ,related_name='rec_id'
)
    dm = models.CharField(max_length=1000)
