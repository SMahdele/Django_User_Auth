from django.urls import path
from .views import FollowUserView,FollowersView


urlpatterns = [   path('follow/<str:pk>/',FollowUserView.as_view(), name="follow"),
                  path('followers/',FollowersView.as_view(), name="followers"),
                  ]
