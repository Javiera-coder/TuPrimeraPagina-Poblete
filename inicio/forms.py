from django import forms

class CrearPrenda(forms.Form):
    marca = forms.CharField(max_length=20)
    categoria = forms.CharField(max_length=20)
    talla = forms.CharField(max_length=5)

class BuscarPrenda(forms.Form):
    categoria = forms.CharField(max_length=20, required=False)
