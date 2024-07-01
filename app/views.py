from django.shortcuts import render, redirect
from .models import Servicos
from django.views.generic import CreateView
from django.urls import reverse_lazy
import json
from django.http import JsonResponse
from django.urls import reverse_lazy
# Create your views here.

from .models import Servicos

def home (request):
    return render(request,"home.html")

def servicos (request):
    return render(request,"servicos.html")

class Savez(CreateView):
    model=Servicos
    fields=[
        'titulo','descricao','localizacao',
   ]
    template_name='servicos.html'
    success_url=reverse_lazy('salvar')

def servicos (request):
    if request.method =='get':
        servico=Servicos.objects.all()
        print (servico)
    return render(request,"servicos.html")

def cadastrar (request):
    titulo=request.POST.get('titulo')
    descricao=request.POST.get('descricao')
    localizacao=request.POST.get('localizacao')
    Servicos.objects.create(titulo = titulo, descricao = descricao, localizacao = localizacao)
    return redirect(reverse_lazy('servicos'))