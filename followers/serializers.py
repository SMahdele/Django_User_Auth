from rest_framework import serializers
from authentication.models import User
from .models import Follower


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model= Follower
        fields= ['uid','followed_by']

class FollowRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Follower
        fields= ['requested_by','uid']


class FollowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Follower
        fields=['user','uid']

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Follower
        fields=['user','uid']