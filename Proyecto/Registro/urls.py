from django.urls import path, include
from .views import Registro


urlpatterns = [
    path('', Registro.as_view())
]
