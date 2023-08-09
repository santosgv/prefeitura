from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.messages import constants
from login.models import Usuario
from .models import Chamado


def logge(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario']).nome
        return render(request, 'html/inig.html')
    else:
        return redirect('/login/gestor')

def cadi(request):
    return render(request, 'html/cadi.html')


def valif(request):
    if request.method == 'POST':

        tipo= request.POST.get('TIPO')
        local= request.POST.get('loca')
        demanda = request.POST.get('de')

        chamado = Chamado( tipo = tipo, localpro = local, demanda = demanda, usuario = usuario)
        chamado.save()
        return HttpResponse(f"{tipo} {local} {demanda}")


        if tipo == 'out':
             messages.error(request, 'Houve um erro')

             return render(request, 'html/cadi.html', {'messages': messages})

        
    return render(request, 'html/cadi.html')