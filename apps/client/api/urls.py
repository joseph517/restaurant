from django.urls import path
from .views import protected_view
from .views import CreateClientView


urlpatterns = [
    path('protected/', protected_view, name='protected_view'),
    path('create_client/', CreateClientView.as_view(), name='create client'),

]
