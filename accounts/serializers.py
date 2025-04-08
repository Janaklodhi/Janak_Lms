from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import CustomUser
import pdb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', "first_name", "last_name"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name']

    def validate_email(self, value):  # ✅ Fixed the typo
        if not value.endswith("@gmail.com"):
            raise serializers.ValidationError("Only Gmail accounts are allowed")
        return value

    def create(self, validated_data):
        # pdb.set_trace() 
        user = CustomUser.objects.create_user(**validated_data)
        return user




# from rest_framework import serializers
# from .models import CustomUser  # 👈 your custom model

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, min_length=6)

#     class Meta:
#         model = CustomUser  # ✅ correct model
#         fields = ['email', 'password', 'first_name', 'last_name', 'phone_number']

#     def validate_email(self, value):
#         if not value.endswith("@gmail.com"):
#             raise serializers.ValidationError("Only Gmail accounts are allowed")
#         return value

#     def create(self, validated_data):
#         return CustomUser.objects.create_user(**validated_data)  # ✅ make sure CustomManager has create_user
