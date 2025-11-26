from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from usuarios.forms import FormularioRegistro


def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("inicio")
    else:
        form = AuthenticationForm()

    return render(request, "login_usuario.html", {"form": form})


def registro(request):
    if request.method == "POST":
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = FormularioRegistro()

    return render(request, "registro.html", {"form": form})

def logout_usuario(request):
    logout(request)
    return render(request, "logout.html")