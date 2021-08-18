from django.shortcuts import render

# Create your views here.
from .models import Tweets
from rest_framework import viewsets
from .serializer import TweetsSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.contrib.auth.models import User

class TweetsViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Tweets.objects.all()
    # The serializer class for serializing output
    serializer_class = TweetsSerializer
    # optional permission class set permission level
    permission_classes = [permissions.IsAuthenticated]
     #Coule be [permissions.IsAuthenticated]
    def create(self, request,*args,**kwargs):
        author_id = request.user.pk
        user_object = User.objects.filter(id=author_id)
        message = request.data.get("message")
        date = request.data.get("date")
        to_serialize = Tweets.objects.create(author=user_object[0],message=message,date=date)
        # to_serialize.likes.add(author_id)
        serializer = TweetsSerializer(to_serialize, many=False)
        return Response(serializer.data)
        
class LikeTweetView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TweetsSerializer
    queryset = Tweets.objects.all()

    def put(self, request,*args,**kwargs):
        tweet_id = request.data.get("tweet_id")
        tweet_object = Tweets.objects.filter(id=tweet_id)
        tweet_object[0].likes.add(request.user.pk)
        serializer = TweetsSerializer(tweet_object, many=True)
        return Response(serializer.data)
