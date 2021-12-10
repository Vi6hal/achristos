from django.db.models import fields
from rest_framework import serializers
from .models import AppRegistery

class AppRegisterySerializer(serializers.ModelSerializer):
    class Meta:
        model = AppRegistery
        fields= ["url","id","bedtime","last_pinged"]
        read_only_fields = ["last_pinged"]