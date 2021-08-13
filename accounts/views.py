# accounts.views.py

# Here, we are adding all of the necessary imports for our LoginView
# import django_filters.rest_framework
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer, TokenSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# JWT settings
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(generics.CreateAPIView):
    """
    POST user/login/
    """

    # This permission class will overide the global permission class setting
    # Permission checks are always run at the very start of the view, before any other code is allowed to proceed.
    # The permission class here is set to AllowAny, which overwrites the global class to allow anyone to have access to login.
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(data={
                # using DRF JWT utility functions to generate a token
                "token": str(refresh.access_token),
                "refresh": str(refresh),
                })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class RegisterUsersView(generics.CreateAPIView):
    """
    POST user/signup/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password or not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields =['username','email']