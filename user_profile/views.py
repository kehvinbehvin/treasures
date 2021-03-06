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

    def create(self, request,*args,**kwargs):
        # print("hello")
        user_id = request.user.pk
        user_object = User.objects.filter(id=user_id)
        nickname = request.data.get("nickname")
        address = request.data.get("address")
        age = request.data.get("age")
        about_me = request.data.get("about_me")
        image_src = request.data.get("image_src")
        image_src_default = "https://c.files.bbci.co.uk/16620/production/_91408619_55df76d5-2245-41c1-8031-07a4da3f313f.jpg"
        to_serialize = UserProfile.objects.create(user_id=user_object[0], nickname=nickname, address=address, age=age, about_me=about_me, image_src=image_src)
        # to_serialize.likes.add(author_id)
        serializer = ProfileSerializer(to_serialize, many=False)
        return Response(serializer.data)

class IndividualView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
    
    def get(self, request):
        id = request.user.pk
        user_profile = UserProfile.objects.filter(user_id=id)
        serializer = ProfileSerializer(user_profile, many = True)
        return Response(serializer.data)

    def put(self, request,friend_id ,*args,**kwargs):
        print(request)

        id = request.user.pk
        friend_id = friend_id

        user_profile_array = UserProfile.objects.filter(user_id=id)
        friend_profile_array = UserProfile.objects.filter(user_id=friend_id)

        user_array = User.objects.filter(id = id)
        friend_array = User.objects.filter(id=friend_id)

        friend_profile_array[0].friends.add(user_array[0])
        user_profile_array[0].friends.add(friend_array[0])
        friend_serializer = ProfileSerializer(friend_profile_array, many = True)

        serializer = ProfileSerializer(user_profile_array, many = True)

        return Response(serializer.data)



