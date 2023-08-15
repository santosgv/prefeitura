from django.urls import path
from . import  views

urlpatterns = [
    path('adm/', views.adm, name='adml'),
    path('valida_adm', views.val, name='validas_adm')
]