from django.urls import path
from . import  views

urlpatterns = [ 
    path('home/', views.logge, name='home'),
    path('home/<int:page>/', views.logge, name='home'),
    path('cadastro/', views.cadi, name='cadastro'),
    path('validafor/',views.valif,name='form'),
    path('adm/', views.adm, name = 'adm'),
    path('adm/<int:page>/', views.adm, name='adm'),
    path('solucao/', views.admcad, name='admcad'),
    path('solucao/<int:id_chamado>/', views.admcad, name='admcad')
]