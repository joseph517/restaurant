from apps.client.api.serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer
from apps.client.models import Client 
from rest_framework import generics, status
from rest_framework.response import Response
from apps.client.api.serializers import ClientSerializer 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class TokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "Esta es una vista protegida"})

class CreateClientView(generics.CreateAPIView):
    queryset = Client.objects.all() 
    serializer_class = ClientSerializer 
    permission_classes = [AllowAny]