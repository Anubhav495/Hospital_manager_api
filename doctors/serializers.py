from rest_framework import serializers
from doctors.models import Doctor

class Doctor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','name','contact']


