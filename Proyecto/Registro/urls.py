from django.urls import path, include
from .views import Registro, login


urlpatterns = [
    path('', Registro.as_view()),
    path('login/', login)
]
