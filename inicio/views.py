from django.shortcuts import render
from .models import Prenda

def inicio(request):
    return render(request, 'inicio.html')

def otra(request):
    return render(request, 'otra.html')

def crear_prenda(request, marca, categoria, talla):
    prenda = Prenda(marca=marca, categoria=categoria, talla=talla)
    prenda.save()
    return render(request, 'crear_prenda.html', {'prenda': prenda})

def listado_prendas(request):
    prenda = Prenda.objects.all()
    return render(request, 'listado_prendas.html', {'listado_de_prendas': prenda})