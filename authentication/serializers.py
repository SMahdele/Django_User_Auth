from rest_framework import serializers
from .models import User
import uuid
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    uid = serializers.UUIDField(default= uuid.uuid4)

    class Meta:
        model = User
        fields = ['email', 'password','uid']

    def validate(self, attrs):
        email = attrs.get('email', 'password')
        return attrs


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EmailVerificationSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(default= uuid.uuid4)

    class Meta:
        model = User
        fields = ['uid']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['email','password']


class ForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['email']


class ResetPasswordSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(max_length=100,write_only=True)
    class Meta:
        model= User
        fields=['password','confirm_password']


class ReadProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['uid', 'email']

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['uid','is_private','email' ]