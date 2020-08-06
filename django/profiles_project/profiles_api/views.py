from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as functions (get, post, path, put, delete)',
            'it is simila r to a traditional Django view',
            'Gives you the most control over ypur logic',
            'Is mapped manually to URLs'
        ]
        return Response({
            'message': 'Hello!',
            'an_apiview': an_apiview
        })
    def post(self, request):
        """Create a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({
                'message':message
            })
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        return Response({'method':'put'})
    
    def patch( self, request, pk=None ):
        return Response({'method':'patch'})
    def delete( self, request, pk=None ):
        return Response({'method':'delete'})
