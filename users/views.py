from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, LoginSerializer, AllUserSerializer, ChangePasswordSerializer
from .models import User
import jwt, datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')


        response = Response()

        response.data = {
            'message': "Login Success",
            'username': user.username,
            'password': user.password,
            'name': user.name,
            'mobile': user.mobile,
            'user': user.description

        }
        return response


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AllUserSerializer


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout Success'
        }
        return response


class ChangePasswordView(generics.CreateAPIView):
    serializer_class = ChangePasswordSerializer
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        
        username = request.data['username']
        password = request.data['password']
        new_password = request.data['new_password']

        user = User.objects.filter(username=username).first()
        print(user)
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')


        user_new_pass = make_password(new_password)
        user = User.objects.filter(username=username).update(password=user_new_pass)
        response = Response()

        response.data = {
            'message': "Password Change Success",

        }
        return response

