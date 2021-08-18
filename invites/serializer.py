from .models import Invites
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username")
class InvitesSerializer(serializers.ModelSerializer):
    inviter = UserSerializer(many=False)
    invitee = UserSerializer(many=False)
    class Meta:
        # The model it will serialize
        model = Invites
        # the fields that should be included in the serialized output
        fields = ['id','inviter', 'invitee', 'status']
        depth = 1