from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)    

    if not user:
        messages.error(request, 'usuario ou senha invalidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso')
        return redirect('dashboard')

def logout(request):
    return render(request, 'accounts/logout.html')


def signup(request):
    if request.method != 'POST':
        return render(request, 'accounts/signup.html')
    
    nome = request.POST.get("nome")
    sobrenome = request.POST.get("sobrenome")
    usuario = request.POST.get("usuario")
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    senha2 = request.POST.get("senha2")

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, "Precisa preencher os campos!")
        return render(request, 'accounts/signup.html')

    try:
        validate_email(email)
    except:
        messages.error(request, "EMail inválido")
        return render(request, 'accounts/signup.html')

    if len(senha) < 6:
        messages.error(request, "Senha precisa ter 6 digitos ou mais ")
        return render(request, 'accounts/signup.html')         

    if senha != senha2:
        messages.error(request, "Senhas precisam ser iguais ")
        return render(request, 'accounts/signup.html')     

    if User.objects.filter(username=usuario).exists():
        messages.error(request, "Usuário já existe")
        return render(request, 'accounts/signup.html') 

    if User.objects.filter(email=email).exists():
        messages.error(request, "EMail já existe")
        return render(request, 'accounts/signup.html')  

    messages.success(request, "Registado!, faça login")         

    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()

    return redirect('login')      

@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')     