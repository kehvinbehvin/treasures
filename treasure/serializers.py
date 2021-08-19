from rest_framework import serializers
from .models import Treasure
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","id"]

class TreasuresSerializer(serializers.ModelSerializer):
    hunters = UserSerializer(many=True)
    class Meta:
        model = Treasure
        fields = ('author', 'name','description', 'lng','lat','date','hunters','quiz','mcq1','mcq2','mcq3','hint','answer')
        depth = 1