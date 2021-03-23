from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserProjectSerializer, UserEducationSerializer,UserExperienceSerializer
from rest_framework.response import Response
from authentication.models import  User
from .models import UserEducation, UserProject,UserExperience
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import *


# Create your views here.

class UserProjectView(generics.GenericAPIView):
    serializer_class=UserProjectSerializer

    def post(self,request,*args,**kwargs):
            projects=self.request.data
            serializer = self.serializer_class(data=projects)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            #_data=serializer.data
            return Response({'data': serializer.data})

class UserProjectDetails(APIView):

    serializer_class=UserProjectSerializer
    def get(self,request,pk):
            projects=UserProject.objects.filter(user=pk)
            serializer = UserProjectSerializer(projects, many=True)
            return Response({
                        'data':serializer.data
                   })
    def put(self,request,pk):
        id= request.data['id']
        project = UserProject.objects.get(id=id)
        serializer = self.serializer_class(instance=project,data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})

    def delete(self,rquest,pk):
        project = UserProject.objects.filter(user=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserExperienceView(generics.GenericAPIView):
    serializer_class=UserExperienceSerializer

    def post(self,request,*args,**kwargs):
            projects=self.request.data
            serializer = self.serializer_class(data=projects)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            #_data=serializer.data
            return Response({'data': serializer.data})
class UserExperienceDetails(APIView):
    serializer_class=UserExperienceSerializer

    def get(self,request,pk):
            experiences=UserExperience.objects.filter(user=pk)
            serializer = serializer_class(experiences, many=True)
            return Response({
                        'data':serializer.data})

    def put(self, request, pk):
        id = request.data['id']
        experience = UserExperience.objects.get(id=id)
        serializer = self.serializer_class(instance=experience, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})

    def delete(self, rquest, pk):
        experience = UserExperience.objects.filter(user=pk)
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserEducationView(generics.GenericAPIView):
    serializer_class=UserEducationSerializer

    def post(self,request,*args,**kwargs):
            education=self.request.data
            serializer = self.serializer_class(data=education)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            #_data=serializer.data
            return Response({'data': serializer.data})
class UserEducationDetails(APIView):

    serializer_class=UserEducationSerializer
    def get(self,request,pk):
            education=UserEducation.objects.filter(user=pk)
            serializer = UserEducationSerializer(education, many=True)
            return Response({
                        'data':serializer.data
                   })
    def put(self,request,pk):
        id= request.data['id']
        education = UserEducation.objects.get(id=id)
        serializer = self.serializer_class(instance=education,data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})

    def delete(self, rquest, pk):
        education = UserEducation.objects.filter(user=pk)
        education.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)