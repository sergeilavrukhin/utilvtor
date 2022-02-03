from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('firstname', 'phone')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(help_text='Профиль пользователя')

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')
