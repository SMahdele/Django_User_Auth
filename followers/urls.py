from django.urls import path
from .views import FollowUserView #,FollowedbyRequestedbyListView


urlpatterns = [   path('follow-user/<str:pk>/',FollowUserView.as_view(), name="followed_by"),
                  # path('follow-request/',FollowedbyRequestedbyListView.as_view(), name="requested_by"),
                  ]
