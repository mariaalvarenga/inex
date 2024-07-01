from app import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicos/', views.servicos, name='servicos'),
    path('cadastro/', views.cadastrar, name= 'cadastro')
    
]