from rest_framework.views import APIView
from rest_framework import generics
from .models import Follower
from authentication.models import User
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import FollowUserSerializer, FollowRequestSerializer
from user.permissions import IsAuthenticatedOrOwnerOrAdmin,IsOwnerOrReadOnly

# Create your views here.

class FollowUserView(APIView):
    serializer_class= FollowUserSerializer
    model_class=Follower
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin,IsOwnerOrReadOnly]

    def post(self, request, pk,*args,**kwargs):
        try:
            # import pdb; pdb.set_trace()
            user_to_follow= User.objects.get(pk=pk)
            user=request.user
            follower= Follower()
            follower.save()
            if user_to_follow == user:
                return Response({'message': "invalid operation"})
            if user_to_follow.is_private:
                follower.requested_by.add(user_to_follow,user)
                # requests=follower.requested_by.values()
                # print(requests)
                serializer = FollowUserSerializer(data={**request.data, **{"requested_by": request.user.pk}})
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

                return Response({'status':True,
                                 'message':'follow request sent',
                                 "requested_by":serializer.data})
            else:
                    follower.followed_by.add(user_to_follow,user)
                    serializer = FollowUserSerializer(data={**request.data, **{"followed_by": request.user.pk}})
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()

            # list=follower.followed_by.all()
                    # print(list)
            return Response({'status': True,
                             'message': 'followed successfully',
                             "followed_by":serializer.data
                             })
        except User.DoesNotExist:
            raise ValidationError('no such profile found')

# class FollowedbyRequestedbyListView(APIView):
#     serializer_class=FollowUserSerializer
#     model_class= Follower



