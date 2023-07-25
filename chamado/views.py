from django.shortcuts import render


def logge(request):
    return render(request, 'html/inig.html')

