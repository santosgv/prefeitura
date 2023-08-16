from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.messages import constants
from login.models import Usuario
from logadm.models import Usuarioa
from .models import Chamado
from django.core.paginator import Paginator
from datetime import date


def logge(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        chamados = Chamado.objects.filter(usuario=usuario) 
        paginator = Paginator(chamados, 4)
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)
        
        return render(request, 'html/inig.html/', {'page':page, 'usuario':usuario})
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
        locall= request.POST.get('loca')
        demanda = request.POST.get('de')
        
        usuario = Usuario.objects.get(id = request.session['usuario'])
        unidade = usuario.get_local()

        chamado = Chamado( tipo = tipo, localpro = locall, demanda = demanda, usuario = usuario, unidade = unidade)
        chamado.save()
        return redirect('/chamado/home/')



        
    return render(request, 'html/cadi.html')

def adm(request):
    
    if request.session.get('usuario'):
        
        usuario = Usuarioa.objects.get(id = request.session['usuario'])
        chamados = Chamado.objects.filter(tecnico=usuario) 
        paginator = Paginator(chamados, 4)
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)
        
        
        return render(request, 'html/hoadm.html', {'page':page, 'usuario':usuario})
    else:
        return redirect('/logadm/adm')
    
def admcad(request, id_chamado):
    if request.session.get('usuario'):
        chamado = Chamado.objects.get(id=id_chamado)
        if request.method == 'POST':
            id_chamado = request.resolver_match.kwargs['id_chamado']
            solucao = request.POST.get('so')
            fim = bool(request.POST.get('fi'))
            
            if fim:
                finalizado = date.today().strftime('%Y-%m-%d')
                chamado.data_finalizado = finalizado
                status = 'Finalizado'
            else:
                pass
            chamado.solucao = solucao
            chamado.status = status
            chamado.save()
            return redirect('/chamado/adm')    



        else:
            return render(request, 'html/admalt.html', {'chamado':chamado})

    
        


    else:
        return redirect('/logadm/adm')