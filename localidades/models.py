from django.db import models

# Create your models here.

class Pais(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    continente = models.CharField(max_length=30, null=False, blank=False)
    
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    sigla = models.CharField(max_length=2, null=True, blank=False)
    regiao = models.CharField(max_length=20, null=True, blank=False, default='Não informado')
    pais = models.ForeignKey(Pais, related_name='estados', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    populacao = models.BigIntegerField(null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='cidades')
    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return f'{self.nome} - {self.estado.sigla} - {self.estado.pais.nome}'