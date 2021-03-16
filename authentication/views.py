from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics,status
from .serializers import RegisterSerializer,EmailVerificationSerializer,LoginSerializer,ForgotPasswordSerializer,ResetPasswordSerializer
from rest_framework.response import Response
from .models import User
from .utils import Util,ResetEmail
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.exceptions import ValidationError
from django.urls import reverse
import uuid
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(generics.GenericAPIView):

    serializer_class=RegisterSerializer

    def post(self,request):
        user=request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        uid=user_data['uid']
        user= User.objects.get(email=user_data['email'])
        #token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')

        absurl= 'http://'+ current_site+ relativeLink+'?token='+uid
        email_body= 'Hi '+'Use below link to verify your email \n'+ absurl
        data = {'email_body':email_body, 'to_email': user.email,'email_subject':'verify your email'}
        Util.send_email(data)
        content = {'Verification link send to email, verify your account', uid}

        return Response(content,status=status.HTTP_200_OK,)


class VerifyEmail(APIView):
    serializer_class = EmailVerificationSerializer

    def get(self,request):
        try:
            token = request.GET['token']

            object = User.objects.get(uid=token)
            print(object)
            object.is_verified = True
            #print('11')
            object.save()
            #print(User.objects.all())

            return Response({"status":True, "message":"User verified successfully", "data":{}})
        except User.DoesNotExist:
            return Response({"No Verification token exists with this token"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer=LoginSerializer
    model_class=User
    def post(self,request):
        try:
            user= self.request.data
            #print(user)
            for field in ['email', 'password']:
                if not user.get(field):
                    return Response({f"{field} is required"}, status.HTTP_400_BAD_REQUEST)
            object = self.model_class.objects.get(
                email=self.request.data['email'])

            if not object.check_password(self.request.data['password']):
                raise ValidationError(detail=f"Incorrect Password")

            serializer_data = LoginSerializer(object)
            user_data = serializer_data.data

            return Response({
                'message': 'Login Successful',
                'data': user_data
            })

        except self.model_class.DoesNotExist:
            content={"user does not exist"}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):

        try:
            user = self.request.data
            if not user.get('email'):
                return Response({f"Email is required"}, status.HTTP_400_BAD_REQUEST)

            object = User.objects.get(email=self.request.data['email'])
            print(object)
            serializer = ForgotPasswordSerializer(object)
            _data = serializer.data
            print(_data)
            relativeLink = "/auth/reset-password/"
            ResetEmail.reset_email(self,request,object, _data, relativeLink)
            content = {'Forgot Password link send to email'}

            return Response(content, status=status.HTTP_200_OK, )

            #ResetEmail.send(request,object, _data, relativeLink)


        except User.DoesNotExist:
            return Response({"User Not Found"}, status.HTTP_400_BAD_REQUEST)
class ResetPasswordView(generics.GenericAPIView):
    serializer_class=ResetPasswordSerializer
    def post(self,request,pk,*args,**kwargs):
        try:
            user=self.request.data
            for field in ['password', 'confirm_password']:
                if not user.get(field):
                    return Response({f"{field} is required"}, status.HTTP_400_BAD_REQUEST)
            password=self.request.data['password']
            confirm_password=self.request.data['confirm_password']
            if password !=confirm_password:
                return Response({"Password Does not Match"}, status.HTTP_400_BAD_REQUEST)
            object = User.objects.get(uid=pk)
            print(object)
            object.set_password(request.data['password'])
            object.save()
            return Response({"status": True, "message": "password changed successfully", "data": {}},
                            status=status.HTTP_201_CREATED)


        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)