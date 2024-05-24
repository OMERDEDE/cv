from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login as auth_login

from .models import CV, Comment, Education, Experience, Skill, UserRegular


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegular
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserRegular.objects.create_user(**validated_data)
        return user
class UserRegularSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegular
        fields = ('id', 'username', 'email')

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'



"""
MODELİ JSON (JavaScript Object Notation) FORMATINA ÇEVİRİYOR

"""