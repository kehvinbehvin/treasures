from rest_framework import serializers
from .models import Direct
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","id"]
class DMSerializer(serializers.ModelSerializer):
    sender = UserSerializer(many=False)
    recipient = UserSerializer(many=False)
    class Meta:
        model = Direct
        fields = ('sender', 'recipient', 'dm')