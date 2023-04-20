from apps.client.api.serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer
from apps.client.models import Client
from apps.utils import CustomIsAuthenticated 
from rest_framework import generics, status
from rest_framework.response import Response
from apps.client.api.serializers import ClientSerializer,ClientUpdateSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class TokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

class CreateClientView(generics.CreateAPIView):
    queryset = Client.objects.all() 
    serializer_class = ClientSerializer 
    permission_classes = [AllowAny]


class UpdateClientView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer
    permission_classes = [CustomIsAuthenticated.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    