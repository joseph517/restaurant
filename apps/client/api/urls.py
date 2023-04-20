from django.urls import path
from .views import CreateClientView, UpdateClientView, DeleteClientView


urlpatterns = [
    path('create_client/', CreateClientView.as_view(), name='create client'),
    path('update/<int:pk>/', UpdateClientView.as_view(), name='update client'),
    path('delete/<int:pk>/', DeleteClientView.as_view(), name='delete client'),
]
