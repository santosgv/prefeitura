from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Usuarioa


def adm(request):
    return render(request, 'html/adm_login.html' )

def val(request):
    matricula = request.POST.get('Matricula')
    senha = request.POST.get('Senha')
    

    usuario = Usuarioa.objects.filter(matricula = matricula).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/logadm/adm/?status=1')
    
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/chamado/adm')