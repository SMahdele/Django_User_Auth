from rest_framework import serializers
from authentication.models import User
import uuid
from .models import  UserProject,UserEducation,UserExperience


class UserProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model= UserProject
        fields=['title','description','start_date','end_date','user']

class UserExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserExperience
        fields=['company_name','designation','start_date','end_date','user']

class UserEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserEducation
        fields= ['degree','start_date','end_date','user']
