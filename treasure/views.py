
# Create your views here.
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import TreasuresSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Treasure
from django.db import models

class TreasuresView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = TreasuresSerializer
    queryset = Treasure.objects.all()

class TreasureView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TreasuresSerializer
    queryset = Treasure.objects.all()
    
    def put(self, request, *args, **kwargs):
        author_id = request.data.get("author")
        hunter_id = request.data.get("hunter")
        treasure_name = request.data.get("name")
        existing_treasure = Treasure.objects.filter(name=treasure_name)
        # print(existing_treasure[0].hunters)
        existing_treasure[0].hunters.add(hunter_id)
        serializer = TreasuresSerializer(existing_treasure, many=True)
        return Response(serializer.data)

    def get(self,request,name,*args,**kwargs):
        print(name)
        existing_treasure = Treasure.objects.filter(name=name)
        serializer = TreasuresSerializer(existing_treasure, many=True)
        return Response(serializer.data)

class TreasureUserView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TreasuresSerializer
    queryset = Treasure.objects.all()

    def get(self,request,*args,**kwargs):
        id = request.user.pk
        participating_treasures = Treasure.objects.filter(hunters__id__contains=id)
        serializer = TreasuresSerializer(participating_treasures, many= True)
        return Response(serializer.data)
        
# class DmViewID(generics.ListAPIView):s
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = DMSerializer
#     queryset = Direct.objects.all()
#     def get (self, request, id, friend_id):
#         to_serialize = Direct.objects.all().filter(models.Q(recipient=id, sender=friend_id) | models.Q(sender=id, recipient=friend_id))
#         serializer = DMSerializer(to_serialize, many=True)
#         # serializer.is_valid()
#         return Response(serializer.data)