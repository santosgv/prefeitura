from django.shortcuts import render
from django.http import HttpResponse

def gestor(request):
    return render(request, 'login.html')
