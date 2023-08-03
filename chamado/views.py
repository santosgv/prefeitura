from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.messages import constants

def logge(request):
    return render(request, 'html/inig.html')


def cadi(request):
    return render(request, 'html/cadi.html')


def valif(request):
    if request.method == 'POST':
        tipo= request.POST.get('TIPO')
        valor = 0


        if tipo == 'out':
             messages.add_message(request, constants.ERROR, "não é da nossa competencia cidadão")
             valor = valor + 1
             return render(request, 'html/cadi.html')
        elif valor == 2:
            return HttpResponse('cadastrado com sucesso')
    return render(request, 'html/cadi.html')