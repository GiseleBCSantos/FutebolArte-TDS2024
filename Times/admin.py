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
    
class CompeticaoInlineAdmin(admin.TabularInline):
    model = Competicao
    extra = 0

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'divisao_atual', 'imagem', 'cidade', 'modalidade')
    search_fields = ('nome',)
    list_filter = ('divisao_atual', 'modalidade')

    inlines = [JogadorInlineAdmin, TituloInlineAdmin, CompeticaoInlineAdmin]

    
    def imagem(self, obj):
        return format_html(f"<img src='{obj.escudo.url}' width=50px height=50px>")
    
@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'imagem', 'time', 'posicao', 'numero_camisa', 'sexo']
    list_filter = ['time', 'posicao', 'sexo']
    search_fields = ['nome']

    def imagem(self, obj):
        url = 'https://placehold.co/50'
        if (obj.foto):
            url = obj.foto.url
        
        return format_html(f"<img src='{url}' width=50px height=50px")

