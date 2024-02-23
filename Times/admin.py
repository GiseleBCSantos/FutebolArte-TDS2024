from django.contrib import admin
from .models import Time, Jogador, Competicao, Titulo
from django.utils.html import format_html

# Register your models here.


class JogadorInlineAdmin(admin.TabularInline):
    model = Jogador
    extra = 0

class TituloInlineAdmin(admin.TabularInline):
    model = Titulo
    extra = 0

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'divisao_atual', 'imagem', 'titulos', 'uf', 'modalidade')
    search_fields = ('nome', 'divisao_atual', 'imagem', 'titulos', 'uf', 'modalidade')
    list_filter = ('divisao_atual', 'modalidade')

    inlines = [JogadorInlineAdmin, TituloInlineAdmin]

    
    def imagem(self, obj):
        return format_html(f"<img src='{obj.escudo.url}' width=50px height=50px>")
    

@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano_conquista', 'colocacao', 'time']
    search_fields = ['nome', 'ano_conquista', 'time']
    list_filter = ['ano_conquista', 'colocacao']


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'imagem', 'time', 'posicao', 'numero_camisa', 'sexo']
    list_filter = ['time', 'posicao', 'sexo']
    search_fields = ['nome', 'time', 'camisa']

    def imagem(self, obj):
        return format_html(f"<img src='{obj.foto.url}' width=50px height=50px")

