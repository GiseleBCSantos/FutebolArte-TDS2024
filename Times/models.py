from django.db import models
from localidades.models import Cidade, Estado, Pais
from PIL import Image


# Create your models here.

class Time(models.Model):
    MODALIDADE_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )
    
    
    nome = models.CharField(max_length=30, blank=False, null=False)
    ano_fundacao = models.IntegerField(blank=False, null=False)
    divisao_atual = models.CharField(max_length=5, blank=False, null=False)
    
    escudo = models.ImageField(upload_to='Times/escudos')
    
    
    titulos = models.IntegerField(blank=False, null=False)
    cidade = models.ForeignKey(Cidade, related_name='times', on_delete=models.CASCADE)
    uf = models.ForeignKey(Estado, related_name='times', on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='times')
    modalidade = models.CharField(max_length=10, choices=MODALIDADE_CHOICES)
    
    def __str__(self):
        return self.nome
    
    
    
class Jogador(models.Model):
    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )
    
    nome = models.CharField(max_length=100, blank=False, null=False)
    foto = models.ImageField()
    time = models.ForeignKey(Time, related_name='Time', on_delete=models.CASCADE)
    posicao = models.CharField(max_length=20, blank=False, null=False)
    numero_camisa = models.IntegerField(blank=False, null=False)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, blank=False, null=False)    


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


