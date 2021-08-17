from .models import Tweets
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","id"]
class TweetsSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False)
    likes = UserSerializer(many=True)
    class Meta:
        # The model it will serialize
        model = Tweets
        # the fields that should be included in the serialized output
        fields = ['id','author', 'message', 'date','likes']
        depth = 1