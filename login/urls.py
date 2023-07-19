from django.urls import path
from . import  views

urlpatterns = [
    path('gestor/', views.gestor, name= 'gestor'),
    path('adm/', views.adm, name='adm')
]