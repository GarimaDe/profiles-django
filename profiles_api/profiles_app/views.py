from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response #Used to return responses from APIView
from rest_framework import status
from profiles_app import serializers
from rest_framework import viewsets
from profiles_app import models
from rest_framework.authentication import TokenAuthentication
from profiles_app import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions(get,post,put,ptch,delete,update)',
            'Is sismilar to traditional to django view but specifically designed to use with APIs',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message' : 'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello msg with our name """
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, 
            status= status.HTTP_400_BAD_REQUEST
            )
    

    def put(self, request, pk=None):
        """Handles updating an object"""
        serializer = self.serializer_class(data = request.data)
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handles partial update of object"""
        serializer = self.serializer_class(data = request.data)
        return Response({'method': 'patch'})
    
    def delete(self, request, pk=None):
        """Delete object from database"""
        return Response({'method':'delete'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return hello message"""
        a_viewset = ['a','b','c','d','e']

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create new hello msg"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, 
            status= status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting object by its id"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Updatea an object"""
        return Response({'http_method':'PUT'})

    def update_partial(self, request, pk=None):
        """Handle partial updating of an object"""
        serializer = self.serializer_class(data = request.data)
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Removing an object"""
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES