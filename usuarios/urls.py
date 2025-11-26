from django.urls import path
from usuarios.views import login_usuario, registro, logout_usuario

urlpatterns = [
    path("login/", login_usuario, name="login"),
    path("logout/", logout_usuario, name="logout"),
    path("registro/", registro, name="registro"),
]

