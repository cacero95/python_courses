from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """User Serializer for a profile objects"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}} # this command indicates this field could be writting not reading

    def create(self, validated_data):
        # create a return a new user
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password']) # make a hash encode for the password
        user.save()
        return user