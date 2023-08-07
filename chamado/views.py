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



        if tipo == 'out':
             messages.error(request, 'Houve um erro')

             return render(request, 'html/cadi.html', {'messages': messages})

        
    return render(request, 'html/cadi.html')