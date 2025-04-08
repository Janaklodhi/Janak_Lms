# Full CRUD Example Using Generic Views
# Agar tum CRUD APIs manually likhne ki jagah Django REST Framework ke Generic Views use karoge, toh code chhota ho jayega aur efficiency badegi.
# from django.urls import path
# from .views import UserListCreateView, UserDetailView, UserUpdateView, UserDeleteVie
# janak_LMs repo name



# ye  dono ka kya kaaamm hai


# i-028f8ced3d6cb5296 (janak-aws)
# PublicIPs: 65.0.21.162    PrivateIPs: 172.31.12.32    i-028f8ced3d6cb5296 (janak-aws)
# PublicIPs: 65.0.21.162    PrivateIPs: 172.31.12.32    



from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

# ✅ GET: List all users | POST: Create a new user
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# ✅ GET: Retrieve a single user
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# ✅ PUT/PATCH: Update user details
class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# ✅ DELETE: Delete a user
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
