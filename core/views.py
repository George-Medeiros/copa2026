from django.shortcuts import render
from .models import Jogo

def home(request):
    # Busca todos os jogos do banco de dados organizados por data e hora
    jogos = Jogo.objects.all().order_by('data_hora')
    
    # Envia os jogos para dentro da nossa página HTML
    return render(request, 'core/home.html', {'jogos': jogos})
