""""
@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html',
        {'form':form})
    
    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request,
        "Erro ao enviar o formulário.")
        # Preenche o formulario
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html',
        {'form':form})

    descricao = request.POST.get('descricao')
    if len(descricao) < 5:
        messages.error(request, 'Descrição precisa ter mais que 5 caracteres.')
          # Preenche o formulario, mantem os dados
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html',
        {'form':form})
    
    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso!')
    redirect('dashboard')
"""