from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato


#meu email nicholasnas@gmail.com

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    # Validar usuario e senha
    user = auth.authenticate(request, username=usuario,password=senha)
    
    if not user:
        messages.error(request, 'Usuário ou senha incorreto.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login realizado')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('index')    

def cadastro(request):
    # messages.success(request, 'cadastrado')
    # pegando oque ta vindo no post
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    # Validando se tem algum campo vazio
    if not nome or not sobrenome or not email or not usuario \
        or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio')
        return render(request, 'accounts/cadastro.html')
    
    # Verificar se email é valido
    try:
        validate_email(email)
    except:
        messages.error(
            request, 'Email inválido!'
        )
        return render(request, 'accounts/cadastro.html')
        
    
    # Verificar senha   
    if len(senha) < 6:
        messages.error(
            request, 'senha precisa ter caracteres ou mais'
        )
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(
            request, 'Senhas não conferem'
        )
        return render(request, 'accounts/cadastro.html')
    
    # Verificando se já existe usuario usuario e  email 
    if User.objects.filter(username=usuario).exists():
        messages.error(
            request, 'Usuário já existe.'
        )
        return render(request, 'accounts/cadastro.html')
    if User.objects.filter(email=email).exists():
        messages.error(
            request, 'Email já existe.'
        )
        return render(request, 'accounts/cadastro.html')
    
    messages.success(request, 'Usuário registrado, agora faça login.')
    # Passou pelas checagem
    user = User.objects.create_user(
        username=usuario, email=email, password=senha,
        first_name=nome, last_name=sobrenome,
    )
    user.save()
    return redirect('login')
   


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
    return redirect('dashboard')