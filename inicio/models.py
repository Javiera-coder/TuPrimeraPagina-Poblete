from django.db import models

class Prenda(models.Model):
    marca = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    talla = models.CharField(max_length=5)
    imagen = models.ImageField(upload_to='imagenes_prendas', null=True)

    def __str__(self):
        return f"{self.id} - {self.marca} - {self.categoria} - {self.talla}"
