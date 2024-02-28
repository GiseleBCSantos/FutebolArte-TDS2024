from django.db import models
from localidades.models import Cidade, Estado, Pais
from PIL import Image


# Create your models here.

class Time(models.Model):
    MODALIDADE_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )
    
    DIVISAO_CHOICES = (
        ('A', 'Série A'), 
        ('B', 'Série B'), 
        ('C', 'Série C'), 
        ('D', 'Série D'), 
        ('S', 'Sem série')
    )
    
    
    nome = models.CharField(max_length=30, blank=False, null=False)
    ano_fundacao = models.IntegerField(blank=False, null=False)
    divisao_atual = models.CharField(choices=DIVISAO_CHOICES, max_length=5, blank=False, null=False)
    
    escudo = models.ImageField(upload_to='Times/escudos')
    
    
    cidade = models.ForeignKey(Cidade, related_name='times', on_delete=models.CASCADE)
    modalidade = models.CharField(max_length=10, choices=MODALIDADE_CHOICES)
    
    def __str__(self):
        return self.nome
    
    
    
class Jogador(models.Model):
    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )

    POSICAO_CHOICES = (
        ('Goleiro', 'Goleiro'),
        ('Zagueiro', 'Zagueiro'),
        ('Lateral', 'Lateral'),
        ('Atacante', 'Atacante')
    )
    
    nome = models.CharField(max_length=100, blank=False, null=False)

    foto = models.ImageField(upload_to='Times/Jogadores')

    time = models.ForeignKey(Time, related_name='Time', on_delete=models.CASCADE)
    posicao = models.CharField(max_length=20, blank=False, null=False, choices=POSICAO_CHOICES)
    numero_camisa = models.IntegerField(blank=False, null=False)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, blank=False, null=False)   

    class Meta:
        verbose_name_plural = 'Jogadores'

    def __str__(self):
        return self.nome 


class Competicao(models.Model):
    TIPO_CHOICES = (
        ('Estadual', 'Estadual'),
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional')
    )
    
    CATEGORIA_CHOICES = (
        ('COPA', 'copa'),
        ('CAMPEONATO', 'campeonato')
    )
    
    nome = models.CharField(max_length=30, blank=False, null=False)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, blank=False, null=False)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.nome 


class Titulo(models.Model):
    COLOCACAO_CHOICES = (
        ('1°', '1° Lugar'),
        ('2°', '2° Lugar'),
        ('3°', '3° Lugar'),
    )
    nome = models.CharField(max_length=50, blank=False, null=False)
    ano_conquista = models.IntegerField(blank=False, null=False)
    colocacao = models.CharField(choices=COLOCACAO_CHOICES, max_length=10, blank=False, null=False)

    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='Times')

    
    def __str__(self):
        return self.nome