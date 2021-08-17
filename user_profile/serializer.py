from .models import UserProfile
from rest_framework import serializers

# Our TodoSerializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        # The model it will serialize
        model = UserProfile
        # the fields that should be included in the serialized output
        fields = ['id','user_id', 'nickname', 'address', 'age', 'about_me', 'friends']