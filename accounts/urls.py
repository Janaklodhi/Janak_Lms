from django.urls import path, include
from .views import RegisterView , LoginView, LogoutView, ListData, UserViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [

    path('', include(router.urls)), 
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),  # Added missing `/
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("users/", ListData.as_view(), name="users" ),
    ]