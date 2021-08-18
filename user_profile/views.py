from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from .models import UserProfile
from rest_framework import generics, viewsets
from rest_framework import permissions
from .serializer import ProfileSerializer

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

class IndividualView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
    
    def get(self, request):
        id = request.user.pk
        user_profile = UserProfile.objects.filter(user_id=id)
        serializer = ProfileSerializer(user_profile, many = True)
        return Response(serializer.data)

    def put(self, request):
        # Should be able to add friends
        pass

