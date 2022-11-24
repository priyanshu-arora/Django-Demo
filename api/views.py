from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
# Create your views here.

def home(request):
    return HttpResponse("Hi There!")
@api_view(['GET'])
def getStudent(request):
    obj = Student.objects.all()
    serializer = StudentSerializer(obj,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerStudent(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

