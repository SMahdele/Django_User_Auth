from rest_framework.views import APIView
from .serializers import UserPostSerializer, CommentSerializer, PostLikeDislikeSerializer
from .models import UserPost, Comment
from rest_framework import generics
from rest_framework.response import Response
from authentication.models import User
from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from user.permissions import IsAuthenticatedOrOwnerOrAdmin, IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination, CursorPagination
from .pagination import PostsPagination, CommentsPagination


# Create your views here.

class PostUpdateDeleteView(APIView):
    serializer_class = UserPostSerializer
    model_class = UserPost
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_post(self,request, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise ValidationError("No post found with this id")

    def get(self, request, id):
        obj = self.get_post(request, id=id)
        self.check_object_permissions(self.request, obj)
        serializer = self.serializer_class(obj)
        return Response({
            'status': True,
            'message': "post have following content",
            'data': serializer.data
        })

    def put(self, request, id):
        try:
            post = self.get_post(request, id=id)
            serializer = self.serializer_class(instance=post,
                                               data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': "post updated successfully",
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)

    def delete(self, request, id):
        post = self.get_post(request, id=id)
        post.delete()
        return Response({"message": "post does not exist"})


class CreateReadPostView(generics.ListAPIView):
    serializer_class = UserPostSerializer
    model_class = UserPost
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    pagination_class = PostsPagination

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': ' post created successfully',
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)
        except Exception as e:
            return Response(str(e))

    def get(self, request):
        posts = self.model_class.objects.filter(user=request.user.pk)
        serializer = self.serializer_class(posts, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class CommentView(generics.ListAPIView):
    serializer_class = CommentSerializer
    model_class = Comment
    pagination_class = CommentsPagination

    def get(self,request,id):
        comments = Comment.objects.filter(post=id)
        serializer = self.serializer_class(comments, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

    def post(self, request, id, *args, **kwargs):
        try:
            post = UserPost.objects.get(id=id)
            serializer = self.serializer_class(data={**self.request.data, **{"comment_by": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save(post=post)
                return Response({'status': True,
                                 'message': ' comment added successfully',
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)


class CommentUpdateDeleteView(APIView):
    serializer_class=CommentSerializer
    model_class=Comment
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_obj(self,request,id):
       try:
           # import pdb; pdb.set_trace()
           return self.model_class.objects.get(id=id)
       except self.model_class.DoesNotExist:
           raise ValidationError("No comment found with this id")

    def get(self, request, id):
        obj = self.get_obj(request, id=id)
        self.check_object_permissions(self.request, obj)
        serializer = self.serializer_class(obj)
        return Response({
            'status': True,
            'message': "comment ",
            'data': serializer.data
        })
    def put(self, request, id):
        try:
            comment = self.get_obj(request, id=id)
            serializer = self.serializer_class(instance=comment,
                                               data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': "comment updated successfully",
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)

    def delete(self, request, id):
        comment = self.get_obj(request, id=id)
        comment.delete()
        return Response({"message": "comment with this id does not exist"})


class PostLikeDislikeView(APIView):
    serializer_class = PostLikeDislikeSerializer
    model_class = UserPost

    def post(self, request, id,*args,**kwargs):
        try:
            post = UserPost.objects.get(id=id)
            user = request.user.pk
            if post.liked_by.filter(pk=user).exists():
                post.liked_by.remove(user)
                return Response({'status': True,
                                 'message': "post disliked successfully"})
            else:
                post.liked_by.add(user)
                return Response({'status': True,
                                 'message': 'post liked successfully'})
        except UserPost.DoesNotExist:
            raise ValidationError('no such post found')
