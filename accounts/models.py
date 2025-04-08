from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import *
class CustomUser(AbstractUser):
    username = None  # Remove username field from AbstractUser
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)  # Fixed typo here
    is_phone_no_verified = models.BooleanField(default=False)

    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    
    # Role flags
    is_instructor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)  # every user is at least a student
    is_verified_instructor = models.BooleanField(default=False)
    
     # Permissions & meta
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    

    objects = CustomManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Required when creating a superuser

    def __str__(self):
        return self.email




class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=[("male", "Male"), ("female", "Female")], blank=True, null=True)




class OTPVerification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    purpose = models.CharField(max_length=20, choices=[("email", "Email"), ("phone", "Phone")])
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)


class UserActivityLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
