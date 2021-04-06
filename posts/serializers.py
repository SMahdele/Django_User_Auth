from rest_framework import serializers
from authentication.models import User
from .models import UserPost, Comment


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = ['user', 'post']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'comment_by', 'post']


class PostLikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = ['liked_by', 'post', 'user']
