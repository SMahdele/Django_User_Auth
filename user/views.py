from rest_framework import generics, status
from .serializers import UserProjectSerializer, UserEducationSerializer, UserExperienceSerializer
from rest_framework.response import Response
from authentication.models import User
from .models import UserEducation, UserProject, UserExperience
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import *
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import ValidationError


# Create your views here.

class UserProjectView(APIView):
    serializer_class = UserProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get(self, request):
        pk = request.user.pk
        projects = UserProject.objects.filter(user=pk)
        serializer = UserProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': 'project details added successfully',
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)
        # except Exception as e:
        #     return Response(str(e))


class UserProjectDetails(APIView):
    serializer_class = UserProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_obj(self, request, id):
        try:
            return UserProject.objects.get(id=id)
        except UserProject.DoesNotExist:
            raise ValidationError("No project found with this id")

    def get(self, request, id):
        project = self.get_obj(request, id=id)
        serializer = UserProjectSerializer(project)
        return Response({
            'status': True,
            'message': "user project details",
            'data': serializer.data
        })

    def put(self, request, id):
        try:
            project = self.get_obj(request, id=id)
            serializer = self.serializer_class(instance=project,
                                               data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': " project updated successfully",
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)

    def delete(self, request, id):
        project = self.get_obj(request, id=id)
        project.delete()
        return Response({"message": "user details does not exist"})


class UserExperienceView(generics.GenericAPIView):
    serializer_class = UserExperienceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get(self, request):
        pk = request.user.pk
        experience = UserExperience.objects.filter(user=pk)
        serializer = UserExperienceSerializer(experience, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            experience = self.request.data
            serializer = self.serializer_class(data={**experience, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': 'experience details added successfully',
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)


class UserExperienceDetails(APIView):
    serializer_class = UserExperienceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_obj(self, request, id):
        try:
            return UserExperience.objects.get(id=id)
        except UserExperience.DoesNotExist:
            raise ValidationError("No experience found with this id")

    def get(self, request, id):
        experiences = self.get_obj(request, id=id)
        serializer = UserExperienceSerializer(experiences)
        return Response({
            'status': True,
            'message': "user experience details ",
            'data': serializer.data
        })

    def put(self, request, id):
        try:
            experience = self.get_obj(request, id=id)
            serializer = self.serializer_class(instance=experience,
                                               data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': " experience updated successfully",
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)

    def delete(self, request, id):
        experience = self.get_obj(request, id=id)
        experience.delete()
        return Response({"message": "user details does not exist"})


class UserEducationView(generics.GenericAPIView):
    serializer_class = UserEducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get(self, request):
        pk = request.user.pk
        education = UserEducation.objects.filter(user=pk)
        serializer = UserEducationSerializer(education, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            education = self.request.data
            serializer = self.serializer_class(data={**education, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': 'education details added successfully',
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)


class UserEducationDetails(APIView):
    serializer_class = UserEducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_obj(self, request, id):
        try:
            return UserEducation.objects.get(id=id)
        except UserEducation.DoesNotExist:
            raise ValidationError("No education details found with this id")

    def get(self, request, id):
        education = self.get_obj(request, id=id)
        serializer = UserEducationSerializer(education)
        return Response({
            'status': True,
            'message': "user education details",
            'data': serializer.data
        })

    def put(self, request, id):
        try:
            education = self.get_obj(request, id=id)
            serializer = self.serializer_class(instance=education,
                                               data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': " education details updated successfully",
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)

    def delete(self, request, id):
        education = self.get_obj(request, id=id)
        education.delete()
        return Response({"message": "user details does not exist"})
