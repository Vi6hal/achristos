from datetime import datetime
from django.db.models import fields
from django.utils.timezone import make_aware
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from djoser.conf import settings
from djoser import utils
from .models import UserProfile,RandomData
User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("address",)

class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ("profile","first_name","last_name","email","id")
        ref_name = "UserProfile"


class RandomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomData
        fields = "__all__"