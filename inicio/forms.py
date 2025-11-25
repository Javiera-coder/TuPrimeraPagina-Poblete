from django import forms

class CrearPrenda(forms.Form):
    marca = forms.CharField(max_length=20)
    categoria = forms.CharField(max_length=20)
    talla = forms.CharField(max_length=5)