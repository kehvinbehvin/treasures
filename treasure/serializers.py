from rest_framework import serializers
from .models import Treasure

class TreasuresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treasure
        fields = ('author', 'name','description', 'lng','lat','date','hunters','quiz','mcq1','mcq2','mcq3','hint','answer','money')