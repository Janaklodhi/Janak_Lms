# Create your views here.
from django.shortcuts import render
# from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import pdb
from rest_framework import viewsets
from accounts.models import CustomUser  # 👈 import your model
# # yadi merr ko automatically crud chahiye toh mme viewsets use karna padega or yadi manully crud chahiye toh mujhe  APIView UserSerializer
# karna padega


# this is make avaiable all the api endpoint for all the crud 
class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# this is also fine
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # 👈 use CustomUser instead of User
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ListData(APIView):
     authentication_classes = [JWTAuthentication] 
     permission_classes = [permissions.IsAdminUser]
     def get(self,request):
          users = CustomUser.objects.all()
          serializer = UserSerializer(users, many=True) 
          return Response({"data": serializer.data}, status=200)

# fine 
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password  = request.data.get('password')
        user = CustomUser.objects.filter(email=email).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=200)
        return Response({"error": "Invalid credentials"}, status=400)
    


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
            try:
                 refresh_token = request.data.get("refresh_token")
                 token = RefreshToken(refresh_token)
                 token.blacklist()
                 return Response({"messages":  "Logout successfully"}, status = 200)
            except Exception:
                 return Response({"errro": "invalid credentials"}, status = 400)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")  # Extract from request body
            # print(refresh_token)
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

            # Try to blacklist the token
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()  # Blacklist refresh token
            except Exception as e:
                return Response({"error": "Invalid or expired refresh token"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

