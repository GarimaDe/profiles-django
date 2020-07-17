from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response #Used to return responses from APIView
from rest_framework import status
from profiles_app import serializers


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