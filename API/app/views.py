from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *


@api_view(['GET'])
def GetUsers(re):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateUser(re):
    UserData=UserSerializer(data=re.data)
    if UserData.is_valid():
        UserData.save()
        return Response(UserData.data,status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
