from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from random import randint
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email_login']
        senha = request.POST['senha_login']
        if User.objects.filter(email=email).exists():
            usuario = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = authenticate(request, username=usuario, password=senha)
            if user is not None:
                login_auth(request, user)
                return redirect('index')
    return render(request, 'login.html')

def logout(request):
    logout_auth(request)
    return redirect('index')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha_gerada = [randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)]
        senha = ''.join([str(i) for i in senha_gerada])
        if not nome.strip():
            messages.error(request, 'O nome não pode estar em branco!')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'O email não pode estar em branco!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        send_mail('Senha da sua conta Tratamento CSV!', 'Guarde bem a sua senha: {}'.format(senha), 'sendemailtratamentocsv@gmail.com', [email], fail_silently=False)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'cadastro.html')