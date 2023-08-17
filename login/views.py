from django.shortcuts import render
from .models import Usuario
from django.shortcuts import redirect
from django.http import HttpResponse


def home(request):
    status = request.GET.get('status')
    return render(request, 'html/login.html', {'status': status})

def gestor(request):
    status = request.GET.get('status')
    return render(request, 'html/login.html', {'status': status})


def valida(request):
    matricula = request.POST.get('Matricula')
    senha = request.POST.get('Senha')
    

    usuario = Usuario.objects.filter(matricula = matricula).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/login/gestor/?status=1')
    
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/chamado/home')

    