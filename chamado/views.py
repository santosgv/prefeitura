from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.messages import constants
from login.models import Usuario
from logadm.models import Usuarioa
from .models import Chamado


def logge(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        chamados = Chamado.objects.filter(usuario=usuario)
        
        return render(request, 'html/inig.html', {'chamados':chamados, 'usuario':usuario})
    else:
        return redirect('/login/gestor')

def cadi(request):

    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        


        return render(request, 'html/cadi.html', {'usuario':usuario})
    else:
        return redirect('/login/gestor')



def valif(request):
    if request.method == 'POST':
        tipo= request.POST.get('TIPO')
        local= request.POST.get('loca')
        demanda = request.POST.get('de')
        usuario = Usuario.objects.get(id = request.session['usuario'])

        chamado = Chamado( tipo = tipo, localpro = local, demanda = demanda, usuario = usuario)
        chamado.save()
        return redirect('/chamado/home/')



        
    return render(request, 'html/cadi.html')

def adm(request):
    if request.session.get('usuario'):
        
        usuario = Usuarioa.objects.get(id = request.session['usuario'])
        
        return render(request, 'html/hoadm.html')
    else:
        return redirect('/logadm/adm')