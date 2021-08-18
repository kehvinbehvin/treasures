"""treasure_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from invites.views import InviterViewSet, InviteeViewSet
from invites.serializer import InvitesSerializer
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
# Models
from accounts.views import LoginView, RegisterUsersView, UserListView
from direct_message.views import DmView, DmViewID
from tweets.views import TweetsViewSet, LikeTweetView
from treasure.views import TreasuresView, TreasureView, TreasureUserView
from user_profile.views import IndividualView, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'tweets', TweetsViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'inviters', InviterViewSet)
router.register(r'invitees', InviteeViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', DmView.as_view()),
    path('messages/<friend_id>', DmViewID.as_view()),
    path('user-profile/', IndividualView.as_view(), name = 'individual-profile'),
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/login/',LoginView.as_view(),name='user-login'),
    path('user/signup/', RegisterUsersView.as_view(),  name='user-signup'),
    path('user/viewall/', UserListView.as_view(), name='user-all'),
    path('treasures/', TreasuresView.as_view(),name = 'all-treasures'),
    path('treasure/<name>', TreasureView.as_view(),name = 'detailed-treasures'),
    path('treasures/participated/', TreasureUserView.as_view(),name='participated-treasures'),
    path('like/tweets/',LikeTweetView.as_view(),name='like-tweet')
]
