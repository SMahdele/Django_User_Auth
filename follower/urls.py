from django.urls import path
from .views import FollowUserView,UnFollowUserView, RequestsListView, FollowersListView

urlpatterns = [ path('follow-user/<str:pk>/', FollowUserView.as_view(), name="followed_by"),
                path('unfollow-user/<str:pk>/', UnFollowUserView.as_view()),
                path('followers/list/', FollowersListView.as_view()),
                path('request/list/', RequestsListView.as_view()),

]