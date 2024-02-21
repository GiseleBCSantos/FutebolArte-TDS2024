from django.db import models

# Create your models here.

class Pais(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    continente = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    regiao = models.CharField(max_length=20, null=False, blank=False)
    pais = models.ForeignKey(Pais, related_name='estados', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    populacao = models.BigIntegerField(null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='cidades')

    def __str__(self):
        return self.nome