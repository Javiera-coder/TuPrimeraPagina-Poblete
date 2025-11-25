from django.shortcuts import render, redirect
from .models import Prenda
from inicio.forms import CrearPrenda
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

def inicio(request):
    return render(request, 'inicio.html')

def otra(request):
    return render(request, 'otra.html')

def crear_prenda(request):
    if request.method == 'POST':
        formulario = CrearPrenda(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
        prenda = Prenda(marca=info.get('marca'), categoria=info.get('categoria'), talla=info.get('talla'))
        prenda.save()
        return redirect('listado')
    else:
        formulario = CrearPrenda()
    return render(request, 'crear_prenda.html', {'formulario': formulario})

def listado_prendas(request):
    prenda = Prenda.objects.all()
    return render(request, 'listado_prendas.html', {'listado_de_prendas': prenda})

class PrendaDetailView(DetailView):
    model = Prenda
    template_name = "detalle_prenda.html"
    context_object_name = "prenda"

class PrendaDeleteView(DeleteView):
    model = Prenda
    template_name = "eliminar_prenda.html"
    success_url = reverse_lazy("listado")

class PrendaUpdateView(UpdateView):
    model = Prenda
    fields = "__all__"         
    template_name = "actualizar_prenda.html"
    success_url = reverse_lazy("listado") 