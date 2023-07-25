from django.urls import path
from . import  views

urlpatterns = [
    path('gestor/', views.gestor, name= 'gestor'),
    path('validalogin', views.valida, name='valida')
    
]