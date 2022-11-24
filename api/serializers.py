from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    roll_number = serializers.IntegerField()
    
    def create(self,validated_data):
        return Student.objects.create(**validated_data)