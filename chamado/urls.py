from django.urls import path
from . import  views

urlpatterns = [ 
    path('home/', views.logge, name='home'),
    path('cadastro/', views.cadi, name='cadastro')
]