from rest_framework import serializers
from .models import Client, Prestataire, Service, Demande, Evaluation
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class PrestataireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestataire
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class DemandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demande
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            try:
                client = Client.objects.get(username=username)
            except Client.DoesNotExist:
                raise serializers.ValidationError('Invalid username')

            if not check_password(password, client.password):
                raise serializers.ValidationError('Invalid password')
            if not client.is_active:
                raise serializers.ValidationError('This account is inactive.')

            attrs['user'] = client
        else:
            raise serializers.ValidationError('Must include "username" and "password"')

        return super().validate(attrs)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
        token = super().get_token(user)
        token['email'] = user.email
        return token