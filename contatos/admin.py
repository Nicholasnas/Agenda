from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email','data_criacao' ,
    'categoria', 'mostrar')
    list_display_links = ('id', 'nome','sobrenome')  # link para a descricao completa do contato
    list_filter = ('nome','sobrenome')  # filtro
    list_per_page = 10  # seja exibido 10 elementos por pagina
    search_fields = ('nome', 'sobrenome', 'telefone')  # campo de busca
    list_editable = ('mostrar', 'telefone')


    

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)  # mandar junto


