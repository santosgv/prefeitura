from django.urls import path
from . import  views

urlpatterns = [ 
    path('home/', views.logge, name='home'),
    path('home/<int:page>/', views.logge, name='home'),
    path('cadastro/', views.cadi, name='cadastro'),
    path('validafor/',views.valif,name='form'),
    path('adm/', views.adm, name = 'adm')
]