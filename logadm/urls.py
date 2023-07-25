from django.urls import path
from . import  views

urlpatterns = [
    path('adm/', views.adm, name='adm'),
    path('valida_adm', views.val, name='validas_adm')
]