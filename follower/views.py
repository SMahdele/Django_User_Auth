from rest_framework.views import APIView
from rest_framework import generics
from .models import Follower
from authentication.models import User
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import FollowUnfollowUserSerializer,FollowRequestSerializer
from user.permissions import IsAuthenticatedOrOwnerOrAdmin,IsOwnerOrReadOnly
from .utils import FollowRequestAcceptDeny

# Create your views here.

class FollowUnfollowUserView(APIView):
    serializer_class= FollowUnfollowUserSerializer
    model_class=Follower
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin,IsOwnerOrReadOnly]
    def post(self,request, pk,*args,**kwargs):
        try:
            # import pdb; pdb.set_trace()
            user_to_follow= User.objects.get(pk=pk)
            qs= Follower.objects.filter(user=request.user)
            obj=qs.first()
            if user_to_follow in obj.followed_by.all():
                obj.followed_by.remove(user_to_follow)
                return Response({'status':True,
                                 'message': 'unfollowed'})
            else:
                obj.followed_by.add(user_to_follow)
            # print(obj.followed_by.all())
            return Response({'status': True,
                             'message': 'followed'})
        except User.DoesNotExist:
            return Response('no such user')

class FollowRequestView(APIView):
    serializer_class = FollowRequestSerializer
    model_class = Follower
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin, IsOwnerOrReadOnly]
    def post(self,request, pk,*args,**kwargs):
        try:
            # import pdb; pdb.set_trace()
            user_to_follow = User.objects.get(pk=pk)
            qs = Follower.objects.filter(user=request.user)
            obj = qs.first()
            if user_to_follow in obj.requested_by.all():
                obj.requested_by.remove(user_to_follow)
                return Response({'status': True,
                             'message':'follow request cancelled'})
            elif user_to_follow.is_private:
                obj.requested_by.add(user_to_follow)
                return Response({'status':True,
                    'message': 'follow request'})
        except User.DoesNotExist:
                return Response('no such user')
