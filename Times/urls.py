from django.contrib import admin
from django.urls import path
from .views import exibirJogadores

urlpatterns = [
    path('jogadores', exibirJogadores)
]