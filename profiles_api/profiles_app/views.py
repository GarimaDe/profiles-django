from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response #Used to return responses from APIView

class HelloApiView(APIView):
    """Test APIView"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions(get,post,put,ptch,delete,update)',
            'Is sismilar to traditional to django view but specifically designed to use with APIs',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message' : 'Hello', 'an_apiview': an_apiview})