from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","id")
class ProfileSerializer(serializers.ModelSerializer):
    friends = UserSerializer(many=True)
    user_id = UserSerializer(many=False)
    class Meta:
        # The model it will serialize
        model = UserProfile
        # the fields that should be included in the serialized output
        fields = ['id','user_id', 'nickname', 'address', 'age', 'about_me', 'friends']
        depth = 1