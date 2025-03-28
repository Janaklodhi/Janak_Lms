from rest_framework import serializers
from django.contrib.auth.models import User
import pdb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', "first_name", "last_name"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def validate_email(self, value):  # ✅ Fixed the typo
        if not value.endswith("@gmail.com"):
            raise serializers.ValidationError("Only Gmail accounts are allowed")
        return value

    def create(self, validated_data):
        # pdb.set_trace() 
        user = User.objects.create_user(**validated_data)
        return user
