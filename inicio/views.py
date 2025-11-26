from django.shortcuts import render, redirect
from .models import Prenda
from inicio.forms import CrearPrenda, BuscarPrenda
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio.html')

def otra(request):
    return render(request, 'otra.html')

@login_required
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

@login_required
def listado_prendas(request):
    formulario = BuscarPrenda(request.GET)

    if formulario.is_valid():
        categoria_a_buscar = formulario.cleaned_data.get('categoria')

        if categoria_a_buscar:
            listado_de_prendas = Prenda.objects.filter(
                categoria__icontains=categoria_a_buscar
            )
        else:
            listado_de_prendas = Prenda.objects.all()
    else:
        listado_de_prendas = Prenda.objects.all()

    return render(request, 'listado_prendas.html', {
        'listado_de_prendas': listado_de_prendas,
        'formulario': formulario,
    })


class PrendaDetailView(LoginRequiredMixin, DetailView):
    model = Prenda
    template_name = "detalle_prenda.html"
    context_object_name = "prenda"

class PrendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Prenda
    template_name = "eliminar_prenda.html"
    success_url = reverse_lazy("listado")

class PrendaUpdateView(LoginRequiredMixin, UpdateView):
    model = Prenda
    fields = "__all__"         
    template_name = "actualizar_prenda.html"
    success_url = reverse_lazy("listado") 