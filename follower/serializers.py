from rest_framework import serializers
from authentication.models import User
from .models import Follower
import uuid

class EachUserSerializer(serializers.ModelSerializer):
    user = serializers.UUIDField(source='user__uid')

    class Meta:
        model = Follower
        fields = ('user',)

class FollowerSerializer(serializers.ModelSerializer):
    followed_by = EachUserSerializer(many=True, read_only= True)
    # requested_by = EachUserSerializer(many=True,read_only=True)

    class Meta:
        model = Follower
        fields = ('followed_by',)

class RequestsListSerializer(serializers.ModelSerializer):
    # followed_by = EachUserSerializer(many=True, read_only= True)
    requested_by = EachUserSerializer(many=True,read_only=True)

    class Meta:
        model = Follower
        fields = ('requested_by',)
