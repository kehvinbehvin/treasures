from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Invites
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import InvitesSerializer
from django.contrib.auth.models import User

# Create your views here.
class InvitesViewSet(viewsets.ModelViewSet):
    queryset = Invites.objects.all()
    serializer_class = InvitesSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request,*args,**kwargs):
        inviter = request.user.pk
        user_object = User.objects.filter(id=inviter)

        invitee = request.data.get("invitee")
        invitee_object = User.objects.filter(id=invitee)

        to_serialize = Invites.objects.create(inviter=user_object[0], invitee=invitee_object[0], status="PENDING")
        
        # to_serialize.likes.add(author_id)
        serializer = InvitesSerializer(to_serialize, many=False)
        return Response(serializer.data)

    def list(self, request, id):
        current_user = id
        user_object = User.objects.filter(id=current_user)

        to_serialize = Invites.objects.filter(inviter=user_object[0])
        serializer = InvitesSerializer(to_serialize)
        return HttpResponse("hello")