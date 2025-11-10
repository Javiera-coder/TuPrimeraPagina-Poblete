from django.urls import path
from inicio.views import inicio, otra, crear_prenda, listado_prendas

urlpatterns = [
    path('', inicio),
    path('otra/', otra),
    path('crear-prenda/<marca>/<categoria>/<talla>/', crear_prenda),
    path('listado-prendas/', listado_prendas)
]