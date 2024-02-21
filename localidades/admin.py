from django.contrib import admin
from .models import Pais, Estado, Cidade

# Register your models here.

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['nome', 'continente']
    search_fields = ['nome', 'continente']
    
    
class PaisInlineAdmin(admin.TabularInline):
    model = Pais
    extra = 0

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'regiao', 'pais']
    search_fields = ['nome']
    
    autocomplete_fields = ['pais']
    inline = [PaisInlineAdmin]


class EstadoInlineAdmin(admin.TabularInline):
    model = Estado
    extra = 0

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'populacao', 'estado']
    autocomplete_fields = ['estado']
    inline = [EstadoInlineAdmin]
    