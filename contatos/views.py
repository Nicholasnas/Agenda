from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value # fazer consultas mais complexas
from django.db.models.functions import Concat  # unir campos
from django.contrib import messages

def index(request):
    contatos_list = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos_list, 10)

    page = request.GET.get('page')
    contatos =  paginator.get_page(page) # mandando lista de contatos
    return render(request, 'contatos/index.html',
    {
        'contatos': contatos,
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html',{
    'contato': contato,
     })
 

def busca(request):
    termo = request.GET.get('termo')

    # Verifica se o campo é None ou esta sem termo
    if termo is None or not termo:
        messages.add_message(request,
            messages.ERROR,
            'Campo termo não pode ficar vazio.'
        )
        return redirect('index')  # nao encontrando redireciona para o index
    else:
          messages.add_message(request,
            messages.SUCCESS,
            'Mensagem de sucesso.'
        )
    

    # Unir campos
    campos = Concat('nome',Value(' '), 'sobrenome')  # Value simula um valor no db
    print(termo)
    # contatos_list = Contato.objects.order_by('-id').filter(
    #     Q(nome__icontains=termo) | Q(sobrenome__icontains=termo), # busca por parte do termo - parcialmente
    #     mostrar=True
    # )

    # Criar um valor do meu nome temporario
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(mostrar=True).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    paginator = Paginator(contatos, 20)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })

