from rest_framework import generics, status
from .serializers import UserProjectSerializer, UserEducationSerializer, UserExperienceSerializer
from rest_framework.response import Response
from authentication.models import User
from .models import UserEducation, UserProject, UserExperience
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import *
from rest_framework import permissions
from .permissions import *
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import filters
from .pagination import *
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class DetailsAPIView(APIView):
    serializer_class = None
    model_class = None

    def get_obj(self, request, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            raise ValidationError("No details found with this id")
    #import pdb; pdb.set_trace()
    def get(self, request, id):
        obj = self.get_obj(request, id=id)
        self.check_object_permissions(self.request,obj)
        serializer = self.serializer_class(obj)
        return Response({
            'status': True,
            'message': "user details",
            'data': serializer.data
        })

    def put(self, request, id):
        try:
            details = self.get_obj(request, id=id)
            serializer = self.serializer_class(instance=details,
                                               data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': "details updated successfully",
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)

    def patch(self, request, id):
        try:
            details = self.get_obj(request, id=id)
            serializer = self.serializer_class(instance=details,partial=True,
                                               data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': " details partially updated.",
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)


    def delete(self, request, id):
        details = self.get_obj(request, id=id)
        details.delete()
        return Response({"message": "user details does not exist"})

class ReadPostAPIView(generics.ListAPIView):
    serializer_class = None
    model_class = None
    # def get_queryset(self):
    #     details = self.model_class.objects.filter(user=request.user.pk)

    #     user = self.request.user
    #     return user.user_set.all()  # queryset = self.filter_queryset(self.get_queryset())

    def get(self, request,*args,**kwargs):
        details = self.model_class.objects.filter(user=request.user.pk)
        serializer = self.serializer_class(details, many=True)
        page= self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': ' details added successfully',
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)
        except Exception as e:
            return Response(str(e))



class UserProjectView(ReadPostAPIView):
    serializer_class = UserProjectSerializer
    model_class = UserProject
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    pagination_class= UserProjectViewPagination
    #filter_backends = [DjangoFilterBackend]


    filter_backends = [filters.SearchFilter,]
    search_fields = ['title', 'description',]

class UserProjectDetails(DetailsAPIView):
    serializer_class = UserProjectSerializer
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin]
    model_class = UserProject

class UserExperienceView(ReadPostAPIView):
    serializer_class = UserExperienceSerializer
    model_class = UserExperience
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    pagination_class= UserExperienceViewPagination
    # filter_backends = [filters.SearchFilter,]
    # search_fields = ['company_name', 'designation',]

class UserExperienceDetails(DetailsAPIView):
    serializer_class = UserExperienceSerializer
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin]
    model_class = UserExperience


class UserEducationView(ReadPostAPIView):
    serializer_class = UserEducationSerializer
    model_class = UserEducation
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,
                          ]
    pagination_class= UserEducationViewPagination
    # filter_backends = [filters.SearchFilter,]
    # search_fields = ['degree',]

class UserEducationDetails(DetailsAPIView):
    serializer_class = UserEducationSerializer
    permission_classes = [IsAuthenticatedOrOwnerOrAdmin]
    model_class = UserEducation