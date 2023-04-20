from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.client.models import Client 

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agregar atributos personalizados al token
        token['nombre'] = user.nombre
        token['apellido'] = user.apellido

        return token

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('correo_electronico', 'password')

    def create(self, validated_data):
        user = Client.objects.create_user(
            correo_electronico=validated_data['correo_electronico'],
            password=validated_data['password'],
        )
        return user

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nombre', 'apellido', 'correo_electronico', 'numero_telefono', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        client = User.objects.create_user(
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            correo_electronico=validated_data['correo_electronico'],
            numero_telefono=validated_data['numero_telefono'],
            password=validated_data['password'],
        )
        return client
    

class ClientUpdateSerializer(ClientSerializer):
    class Meta(ClientSerializer.Meta):
        extra_kwargs = {
            "apellido": {"required": False},
            "correo_electronico": {"required": False},
            "numero_telefono": {"required": False},
        }

class DeleteClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'