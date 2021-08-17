from .models import Tweets
from rest_framework import serializers
from django.contrib.auth.models import User

# Our TodoSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id")
class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        author = UserSerializer(many=False)
        # The model it will serialize
        model = Tweets
        # the fields that should be included in the serialized output
        fields = ['id','author', 'message', 'date']
        depth = 1