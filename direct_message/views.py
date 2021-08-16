from typing import final
from django.shortcuts import render
from .models import Direct
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views import View
import json
from .helpers import GetBody
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

class DmView(View):
    def get (self, request):
        dm = Direct.objects.all()
        serialized = serialize("json", dm)
        final_data = json.loads(serialized)
        print(dm)
        return JsonResponse(final_data, safe=False)

    def post (self, request):
        body = GetBody(request)
        dm = Direct.objects.create(sender_id=body["sender"], recipient_id=body["recipient"], dm=["dm"])
        final_data = json.loads(serialize("json", [dm]))
        return JsonResponse(final_data, safe=False)

class DmViewID(View):
    def get (self, request, id, friend_id):
        sender = Direct.objects.all().filter(Q(recipient=id, sender=friend_id) | Q(sender=id, recipient=friend_id))
        print("SENDER OVER HERE", sender)
        serialized = serialize("json", sender)
        final_data = json.loads(serialized)
        return JsonResponse(final_data, safe= False)