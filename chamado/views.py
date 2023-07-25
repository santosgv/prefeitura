from django.shortcuts import render


def logge(request):
    return render(request, 'html/inig.html')


def cadi(request):
    return render(request, 'html/cadi.html')

