from core.models import Time

def rodar():
    print("Iniciando o cadastro dos grupos reais da Copa 2026...")

    # Mapeamento oficial dos 12 Grupos (A até L) com as 48 seleções
    grupos_reais = {
        "A": ["México", "Coreia do Sul", "África do Sul", "República Tcheca"],
        "B": ["Canadá", "Suíça", "Catar", "Bósnia e Herzegovina"],
        "C": ["Brasil", "Marrocos", "Escócia", "Haiti"],
        "D": ["Estados Unidos", "Austrália", "Paraguai", "Turquia"],
        "E": ["Alemanha", "Equador", "Costa do Marfim", "Curaçao"],
        "F": ["Holanda", "Japão", "Tunísia", "Suécia"],
        "G": ["Bélgica", "Irã", "Egito", "Nova Zelândia"],
        "H": ["Espanha", "Uruguai", "Arábia Saudita", "Cabo Verde"],
        "I": ["França", "Senegal", "Noruega", "Iraque"],
        "J": ["Argentina", "Áustria", "Argélia", "Jordânia"],
        "K": ["Portugal", "Colômbia", "Uzbequistão", "República Democrática do Congo"],
        "L": ["Inglaterra", "Croácia", "Panamá", "Gana"]
    }

    total_criado = 0
    for letra_grupo, selecoes in grupos_reais.items():
        for nome_time in selecoes:
            time, criado = Time.objects.get_or_create(
                nome=nome_time,
                defaults={"grupo": letra_grupo}
            )
            # Se o time já existia mas estava em outro grupo no teste anterior, atualiza para o real
            if not criado and time.grupo != letra_grupo:
                time.grupo = letra_grupo
                time.save()
                
            if criado:
                print(f"[{letra_grupo}] Cadastrado: {nome_time}")
                total_criado += 1

    print(f"\nSucesso! O banco de dados agora conta com todas as 48 seleções nos seus grupos oficiais! 🏆")
    