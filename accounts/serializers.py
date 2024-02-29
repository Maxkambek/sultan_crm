from .models import Account
from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone', 'password']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone', 'name', 'password', 'role', 'get_branch_name', 'created_at']
