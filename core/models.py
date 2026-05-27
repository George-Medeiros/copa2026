from django.db import models

class Time(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    grupo = models.CharField(max_length=1, help_text="Grupos de A até L")

    def __str__(self):
        return f"{self.nome} (Grupo {self.grupo})"

class Jogo(models.Model):
    ETAPAS = [
        ('GRUPO', 'Fase de Grupos'),
        ('R32', 'Dezesseis-avos (32 times)'),
        ('R16', 'Oitavas de Final'),
        ('QF', 'Quartas de Final'),
        ('SF', 'Semifinal'),
        ('TP', 'Disputa de 3º Lugar'),
        ('F', 'Final'),
    ]

    etapa = models.CharField(max_length=5, choices=ETAPAS, default='GRUPO')
    data_hora = models.DateTimeField()
    
    time_casa = models.ForeignKey(Time, on_delete=models.SET_NULL, null=True, blank=True, related_name='jogos_casa')
    time_fora = models.ForeignKey(Time, on_delete=models.SET_NULL, null=True, blank=True, related_name='jogos_fora')
    
    gols_casa = models.PositiveIntegerField(null=True, blank=True)
    gols_fora = models.PositiveIntegerField(null=True, blank=True)
    
    penaltis_casa = models.PositiveIntegerField(null=True, blank=True)
    penaltis_fora = models.PositiveIntegerField(null=True, blank=True)
    
    encerrado = models.BooleanField(default=False)

    # Lógica de cruzamento: de qual jogo anterior vem o time da casa e o de fora
    jogo_origem_casa = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='proximo_jogo_casa')
    jogo_origem_fora = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='proximo_jogo_fora')

    def __str__(self):
        casa = self.time_casa.nome if self.time_casa else "A definir"
        fora = self.time_fora.nome if self.time_fora else "A definir"
        return f"{casa} x {fora} ({self.get_etapa_display()})"
    