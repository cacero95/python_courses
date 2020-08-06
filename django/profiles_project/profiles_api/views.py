from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions
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

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        a_viewset = [
            'Uses actions ( list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    def create(self, request):
        """Create a new Hello message"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Hanldes getting an object by its ID"""
        return Response({'http_method' : 'GET'})
    def update(self, request, pk=None):
        """Handles updatinf in the dba"""
        return Response({'http:method': 'PUT'})
    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})
    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    # handles creating, creating and updating profiles

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) # python interpreta thid like a tuple
    permission_classes = (permissions.UpdateOwnProfile,) # python interpreta thid like a tuple
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    # check the email and password for return a token authentication

    serializer_class = AuthTokenSerializer
    def create(self, request):
        return ObtainAuthToken().post(request)