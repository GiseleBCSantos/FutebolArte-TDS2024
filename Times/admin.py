from django.contrib import admin
from .models import Time, Jogador, Competicao
from django.utils.html import format_html

# Register your models here.

class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'divisao_atual', 'imagem', 'titulos', 'uf', 'modalidade')

    def imagem(self, obj):
        return format_html(f"<img src='{obj.escudo.url}' width=50px height=50px>")
    

admin.site.register(Time, TimeAdmin)


