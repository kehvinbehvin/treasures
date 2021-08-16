from .models import Tweets
from rest_framework import serializers

# Our TodoSerializer
class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        # The model it will serialize
        model = Tweets
        # the fields that should be included in the serialized output
        fields = ['id','author', 'message', 'date']