from .models import Account, FAQ
from rest_framework import serializers


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone', 'password']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone', 'name', 'branch', 'password', 'role', 'get_branch_name', 'created_at']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone', 'name', 'branch', 'role', 'get_branch_name', 'created_at', 'avatar']
