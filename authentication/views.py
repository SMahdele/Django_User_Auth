from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, ForgotPasswordSerializer, \
    ResetPasswordSerializer,ReadProjectSerializer
from rest_framework.response import Response
from .models import User
from .utils import Util, ResetEmail
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.exceptions import ValidationError
from django.urls import reverse
import uuid
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        uid = user_data['uid']
        user = User.objects.get(email=user_data['email'])

        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')

        absurl = 'http://' + current_site + relativeLink + '?token=' + uid
        email_body = 'Hi ' + 'Use below link to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'verify your email'}
        Util.send_email(data)
        return Response( {'Verification link send to email, verify your account': uid}, status=status.HTTP_200_OK, )


class VerifyEmail(APIView):
    serializer_class = EmailVerificationSerializer

    # def get(self, request, pk):
    #     try:
    #         user = User.objects.get(uid=pk)
    #         user.is_verified = True
    #         user.save()
    #         return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
    #
    #     except User.DoesNotExist:
    #         return Response({"Not a valid token"}, status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        try:
            #if request.method== 'GET':
                token = request.GET['token']
                object = User.objects.get(uid=token)
                object.is_verified = True
                object.save()

                return Response({"status": True, "message": "User verified successfully", "data": {}})
        except User.DoesNotExist:
            return Response({"No Verification token exists with this token"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer = LoginSerializer
    model_class = User

    def post(self, request):
        try:
            user = self.request.data
            for field in ['email', 'password']:
                if not user.get(field):
                    return Response({f"{field} is required"}, status.HTTP_400_BAD_REQUEST)
            # object = self.model_class.objects.get(
            #     email=self.request.data['email'])
            object = User.objects.get(email=self.request.data['email'])
            if not object.check_password(self.request.data['password']):
                raise ValidationError(detail=f"Incorrect Password")
            #import pdb;pdb.set_trace()
            token = RefreshToken.for_user(object)
            user_serializer = LoginSerializer(object)
            object_data = user_serializer.data
            object_data.update({'token': str(token.access_token)})

            return Response({
                'message': 'Login Successful',
                'data': object_data
            })

        except self.model_class.DoesNotExist:
            return Response({"user does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):

        try:
            user = self.request.data
            if not user.get('email'):
                return Response({f"Email is required"}, status.HTTP_400_BAD_REQUEST)

            object = User.objects.get(email=self.request.data['email'])
            serializer = ForgotPasswordSerializer(object)
            _data = serializer.data
            relativeLink = "/auth/reset-password/"
            ResetEmail.reset_email(request, object, _data, relativeLink)
            return Response({'Forgot Password link send to email'}, status=status.HTTP_200_OK, )
        except User.DoesNotExist:
            return Response({"User Not Found"}, status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, pk, *args, **kwargs):
        try:
            user = self.request.data
            for field in ['password', 'confirm_password']:
                if not user.get(field):
                    return Response({f"{field} is required"}, status.HTTP_400_BAD_REQUEST)
            password = self.request.data['password']
            confirm_password = self.request.data['confirm_password']
            if password != confirm_password:
                return Response({"Password Does not Match"}, status.HTTP_400_BAD_REQUEST)
            object = User.objects.get(uid=pk)
            object.set_password(request.data['password'])
            return Response({"status": True, "message": "password changed successfully", "data": {}},
                            status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TokenTestingView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class =ReadProjectSerializer

    def get(self, request):
        try:
            user = request.user
            serializer = ReadProjectSerializer(user)
            _data = serializer.data
            return Response({'data': _data})

        except User.DoesNotExist:
            return Response({"Not a valid token"}, status.HTTP_400_BAD_REQUEST)