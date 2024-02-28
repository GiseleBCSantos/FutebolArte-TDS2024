from django.contrib import admin
from .models import Pais, Estado, Cidade

# Register your models here.

class EstadoInlineAdmin(admin.TabularInline):
    model = Estado
    extra = 0
    
class CidadeInlineAdmin(admin.TabularInline):
    model = Cidade
    extra = 0
    

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['nome', 'continente']
    search_fields = ['nome', 'continente']
    
    inlines = [EstadoInlineAdmin]
    
    

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'regiao', 'pais']
    search_fields = ['nome']
    
    autocomplete_fields = ['pais']
    inlines = [CidadeInlineAdmin]

