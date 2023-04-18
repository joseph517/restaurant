from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

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
