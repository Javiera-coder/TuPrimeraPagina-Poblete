from django.urls import path
from inicio.views import inicio, otra, crear_prenda, listado_prendas, PrendaDetailView, PrendaDeleteView, PrendaUpdateView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('otra/', otra, name="otra"),
    path('crear-prenda/', crear_prenda, name="crear"),
    path('listado-prendas/', listado_prendas, name="listado"),
    path("prendas/<int:pk>/", PrendaDetailView.as_view(), name="detalle_prenda"),
    path("prendas/<int:pk>/eliminar/", PrendaDeleteView.as_view(), name="eliminar_prenda"),
    path("prendas/<int:pk>/editar/", PrendaUpdateView.as_view(), name="actualizar_prenda"),
]