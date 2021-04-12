from rest_framework.views import APIView
from rest_framework import generics
from .models import Follower
from authentication.models import User
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import EachUserSerializer,FollowerSerializer,RequestsListSerializer
from user.permissions import IsAuthenticatedOrOwnerOrAdmin,IsOwnerOrReadOnly
from rest_framework.decorators import api_view, action

from .utils import FollowRequestAcceptDeny

# Create your views here.

class FollowUserView(APIView):
    serializer_class= EachUserSerializer
    model_class=Follower
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin,IsOwnerOrReadOnly]

    # @api_view(['POST'])
    def post(self,request, pk):
        # import pdb; pdb.set_trace()
        user_to_follow = User.objects.get(pk=pk)
        follower=Follower()
        follower.save()
        if not user_to_follow== request.user:
            if user_to_follow.is_private:
                follower.requested_by.add(user_to_follow)
                follower.save()
                return Response({'message':'request sent'})
            else:
                follower.followed_by.add(user_to_follow)
                return Response('followed successfully')

class UnFollowUserView(APIView):
    serializer_class=EachUserSerializer
    model_class= Follower
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin,IsOwnerOrReadOnly]

    def post(self,request,pk):
        user= User.objects.get(pk=pk)
        follower= Follower()
        follower.save()
        if user in follower.followed_by.all():
            follower.followed_by.remove(user)
            follower.save()
            return Response('unfollowed successfully')
        if user in follower.requested_by.all():
            follower.requested_by.remove(user)
            follower.save()
            return Response('request cancelled')

class FollowersListView(APIView):
    serializer_class= FollowerSerializer
    model_class=Follower
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin,IsOwnerOrReadOnly]

    def get(self,request):
        user=self.model_class.objects.filter(pk=request.user.pk)
        follower=Follower()
        follower.save()
        followers= follower.followed_by.filter(user=user)
        serializer = self.serializer_class(followers, many=True)
        return Response({'data': serializer.data})

class RequestsListView(APIView):
    serializer_class= RequestsListSerializer
    model_class=Follower
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin,IsOwnerOrReadOnly]

    def get(self,request):
        user=self.model_class.objects.filter(pk=request.user.pk)
        requests = Follower()
        requests.save()
        requested_by = requests.followed_by.filter(user=user)
        serializer = self.serializer_class(requested_by, many=True)
        return Response({'data': serializer.data})







