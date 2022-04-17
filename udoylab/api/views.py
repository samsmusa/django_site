from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from project.models import ImageAlbum, Project
from project.serializers import ImageAlbumSerializer, ImageSerializer, ProjectSerializer, ImageAlbumSerializerPost


@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def project_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True, context={'request': request})
    return Response(serializer.data)



@api_view(['GET'])
def single_project(request, pk):
    """
    List all code snippets, or create a new snippet.
    """
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects, many=False, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def imageAlbum_create(request):
    """
    Create Image ALbum.
    """
    if request.method=='POST':
        serializer = ImageAlbumSerializerPost(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def image_create(request):
    """
    Create Image ALbum.
    """
    if request.method=='POST':
        serializer = ImageSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
