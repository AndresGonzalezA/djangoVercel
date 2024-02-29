# Users/serializers.py
from rest_framework import serializers
from .models import UserLoginAPI, Company, Contact

class UserLoginAPICreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLoginAPI
        fields = ['username', 'password']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__' 

class ContactSerializer(serializers.ModelSerializer):  # Corregido el nombre del serializador
    class Meta:
        model = Contact
        fields = '__all__'
