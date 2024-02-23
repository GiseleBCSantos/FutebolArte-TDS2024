from django.shortcuts import render
from django.http import HttpResponse
from .models import Jogador

# Create your views here.

def exibirJogadores(request):
    jogadores = Jogador.objects.all()
    context = {
        'jogadores': jogadores
    }
    return render(request, 'Times/index.html', context)