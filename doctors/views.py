from django.shortcuts import render
from doctors.models import Doctor
from rest_framework.decorators import api_view
from doctors.serializers import Doctor_serializer,Doctor_Detail_serializer
from django.http import JsonResponse
# Create your views here.

@api_view(['GET'])
def list_doctors(request):
    doctor_list = Doctor.objects.all()
    serializer = Doctor_serializer(doctor_list,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def doctor_detail(request,pk):
    doctor_detail = Doctor.objects.get(pk=pk)
    serializer = Doctor_Detail_serializer(doctor_detail)
    return JsonResponse(serializer.data,safe=False)