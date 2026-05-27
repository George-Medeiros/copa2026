from core.models import Time, Jogo
from django.utils import timezone
from datetime import datetime

def rodar():
    print("Iniciando a inserção de dados da Copa 2026...")

    # 1. Cadastro das 48 Seleções divididas em 12 grupos (A até L)
    dados_times = [
        # Grupo A
        {"nome": "Estados Unidos", "grupo": "A"}, {"nome": "México", "grupo": "A"}, 
        {"nome": "Canadá", "grupo": "A"}, {"nome": "Panamá", "grupo": "A"},
        # Grupo B
        {"nome": "Brasil", "grupo": "B"}, {"nome": "França", "grupo": "B"}, 
        {"nome": "Coreia do Sul", "grupo": "B"}, {"nome": "Mali", "grupo": "B"},
        # Grupo C
        {"nome": "Argentina", "grupo": "C"}, {"nome": "Inglaterra", "grupo": "C"}, 
        {"nome": "Japão", "grupo": "C"}, {"nome": "Marrocos", "grupo": "C"},
        # (Adicione mais times aqui se quiser, ou use estes principais para o teste inicial)
    ]

    times_criados = {}
    for dados in dados_times:
        time, criado = Time.objects.get_or_create(nome=dados["nome"], grupo=dados["grupo"])
        times_criados[time.nome] = time
        if criado:
            print(f"Time cadastrado: {time.nome}")

    # 2. Cadastro de alguns jogos de abertura marcantes
    fuso = timezone.get_current_timezone()
    
    dados_jogos = [
        {
            "casa": "Estados Unidos", "fora": "Panamá", 
            "data": datetime(2026, 6, 11, 17, 0, tzinfo=fuso), "etapa": "GRUPO"
        },
        {
            "casa": "México", "fora": "Canadá", 
            "data": datetime(2026, 6, 11, 20, 0, tzinfo=fuso), "etapa": "GRUPO"
        },
        {
            "casa": "Brasil", "fora": "França", 
            "data": datetime(2026, 6, 12, 16, 0, tzinfo=fuso), "etapa": "GRUPO"
        },
        {
            "casa": "Argentina", "fora": "Marrocos", 
            "data": datetime(2026, 6, 13, 13, 0, tzinfo=fuso), "etapa": "GRUPO"
        },
    ]

    for dj in dados_jogos:
        time_c = times_criados.get(dj["casa"])
        time_f = times_criados.get(dj["fora"])
        
        if time_c and time_f:
            jogo, criado = Jogo.objects.get_or_create(
                time_casa=time_c,
                time_fora=time_f,
                data_hora=dj["data"],
                etapa=dj["etapa"]
            )
            if criado:
                print(f"Jogo cadastrado: {time_c.nome} x {time_f.nome}")

    print("População do banco de dados concluída com sucesso! 🏆")
    