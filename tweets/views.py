from django.shortcuts import render

# Create your views here.
from .models import Tweets
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import TweetsSerializer
# Create your views here.


class TweetsViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Tweets.objects.all()
    # The serializer class for serializing output
    serializer_class = TweetsSerializer
    # optional permission class set permission level
    permission_classes = [permissions.IsAuthenticated] #Coule be [permissions.IsAuthenticated]