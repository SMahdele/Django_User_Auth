from django.shortcuts import render
from rest_framework.views import APIView
# from .serializers import FollowerSerializer
from rest_framework import generics, status
from .models import Follower
from authentication.models import User
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .serializers import *
# Create your views here.

class FollowUserView(APIView):
    serializer_class= FollowUserSerializer
    model_class=Follower
    # permission_classes = [IsAuthenticated]

    def get_user(self,request,pk):
        try:
            # import pdb;
            # pdb.set_trace()
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise ValidationError("No such user found")

    def post(self,request,pk,*args,**kwargs):
        try:
            data=request.data
            serializer = self.serializer_class(data=data)
            if  serializer.is_valid(raise_exception=True):
                serializer.save()

                user_to_follow= self.get_user(request,pk=pk)
                user= self.request.user.uid
                if user_to_follow.is_private:
                    # follower.send_request(another_user)
                    return Response({'status': True,
                             'message': 'follow request sent',
                                 "requested_by": serializer.data['uid'] })

                else:
                    user.add(user_to_follow)
                    return Response({'message': 'following',
                                     'followed_by': serializer.data['uid']})

        except Follower.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class FollowersView(APIView):
    serializer_class=FollowersSerializer
    model_class= Follower

    def get(self,request):
        # if request.method== "GET":
        import pdb; pdb.set_trace()
        user=request.user.uid
        followers=self.model_class.objects.get(pk=user)
        return Response({'followers':followers})

