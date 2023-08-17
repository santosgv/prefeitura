from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home, name ='home'),
    path('gestor/', views.gestor, name= 'gestor'),
    path('validalogin', views.valida, name='valida')
    
]