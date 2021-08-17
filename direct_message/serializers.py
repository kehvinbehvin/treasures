from rest_framework import serializers
from .models import Direct

class DMSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direct
        fields = ('sender', 'recipient', 'dm')