# from typing import final
# from django.shortcuts import render
# from .models import Direct
# from django.http import JsonResponse
# from django.core.serializers import serialize
# from django.views import View
# import json
# from .helpers import GetBody
# from django.contrib.auth.models import User
# from django.db.models import Q
# Create your views here.

# class DmView(View):
#     def get (self, request):
#         dm = Direct.objects.all()
#         serialized = serialize("json", dm)
#         final_data = json.loads(serialized)
#         print(dm)
#         return JsonResponse(final_data, safe=False)

#     def post (self, request):
#         body = GetBody(request)
#         dm = Direct.objects.create(sender_id=body["sender"], recipient_id=body["recipient"], dm=["dm"])
#         final_data = json.loads(serialize("json", [dm]))
#         return JsonResponse(final_data, safe=False)

# class DmViewID(View):
#     def get (self, request, id, friend_id):
#         sender = Direct.objects.all().filter(Q(recipient=id, sender=friend_id) | Q(sender=id, recipient=friend_id))
#         print("SENDER OVER HERE", sender)
#         serialized = serialize("json", sender)
#         final_data = json.loads(serialized)
#         return JsonResponse(final_data, safe= False)


from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import DMSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Direct
from django.db import models

class DmView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DMSerializer
    queryset = Direct.objects.all()

    

class DmViewID(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DMSerializer
    queryset = Direct.objects.all()
    def get (self, request, friend_id):
        id = request.user.pk
        to_serialize = Direct.objects.all().filter(models.Q(recipient=id, sender=friend_id) | models.Q(sender=id, recipient=friend_id))
        serializer = DMSerializer(to_serialize, many=True)
        # serializer.is_valid()
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        # print(request.user.pk)
        sender_id = request.user.pk
        recipient_id = request.data.get("recipient")
        dm = request.data.get("dm")
        to_serialize = Direct.objects.create(sender_id=sender_id, recipient_id=recipient_id, dm=dm)
        serializer = DMSerializer(to_serialize, many=False)
        # serializer = DMSerializer(data={
        #     'sender_id': to_serialize.sender_id,
        #     'recipient_id': to_serialize.recipient_id,
        #     'dm': to_serialize.dm
        # })
        # serializer.is_valid()
        return Response(serializer.data)