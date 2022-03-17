from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'password', 'mobile', 'description']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        refresh = RefreshToken.for_user(instance)

        return instance
    def create_superuser(self, username, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password']


class AllUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','username', 'name', 'password', 'mobile', 'description']        


class ChangePasswordSerializer(serializers.ModelSerializer):
    #old_password = serializers.CharField(max_length=255)
    new_password = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username', 'password', 'new_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    