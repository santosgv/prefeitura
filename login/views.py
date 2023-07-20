from django.shortcuts import render
from django.http import HttpResponse

def gestor(request):
    return render(request, 'html/login.html')


def adm(request):
    return render(request, 'html/login.html' )