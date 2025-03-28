from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import pdb
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ListData(APIView):
    #  pdb.set_trace() 
     authentication_classes = [JWTAuthentication] 
     permission_classes = [permissions.IsAdminUser]
     def get(self,request):
          users = User.objects.all()
          serializer = UserSerializer(users, many=True) 
          return Response({"data": serializer.data}, status=200)
     
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password  = request.data.get('password')
        user = User.objects.filter(username=username).first()

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
                 print(refresh_token)
                 token = RefreshToken(refresh_token)
                 token.blacklist()
                 return Response({"messages":  "Logout successfully"}, status = 200)
            except Exception:
                 return Response({"errro": "invalid credentials"}, status = 400)
            
            
class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")  # Extract from request body
            print(refresh_token)
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

