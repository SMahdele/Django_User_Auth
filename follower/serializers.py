from rest_framework import serializers
from authentication.models import User
from .models import Follower

class FollowUnfollowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('user','followed_by')
class FollowRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follower
        fields = ('user','requested_by',)