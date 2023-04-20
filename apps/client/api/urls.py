from django.urls import path
from .views import CreateClientView, UpdateClientView


urlpatterns = [
    path('create_client/', CreateClientView.as_view(), name='create client'),
    path('update/<int:pk>/', UpdateClientView.as_view(), name='client-update'),
]
