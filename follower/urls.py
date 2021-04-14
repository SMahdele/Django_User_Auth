from django.urls import path
from .views import FollowUnfollowUserView,FollowRequestView

urlpatterns = [ path('follow-user/<str:pk>/', FollowUnfollowUserView.as_view(), name="followed_by"),
                path('follow-req/<str:pk>/', FollowRequestView.as_view()),
                # path('followers/list/', FollowersListView.as_view()),
                # path('request/list/', RequestsListView.as_view()),

]