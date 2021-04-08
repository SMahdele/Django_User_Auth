from rest_framework import serializers
from authentication.models import User
from .models import Follower

class FollowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['uid', 'user' ]#, 'followed_by','requested_by']


class FollowRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['uid', 'user', 'requested_by']
