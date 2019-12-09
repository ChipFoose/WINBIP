from django.contrib import admin
from django.urls import path
from .views import PaginaInicio, Premios, Registro, recuperar, signup, recover, IniciarSesion, postsignup, logout, perfil, plantilla2, inicio2, premios2

urlpatterns = [
    # 1. url de la pagina (PaginaInicio/), 2. el nombre de la funcion, 3. Alias de la pagina
    path('', PaginaInicio, name='inicio'),
    path('premios.html/', Premios, name='premios'),
    path('registro.html/', Registro, name='registro'),
    path('signup/', signup, name='signup'),
    path('iniciarsesion.html', IniciarSesion, name='iniciarsesion'),
    path('postsignup/', postsignup, name='postsignup'),
    path('logout/', logout, name='logout'),
    path('perfil.html/', perfil, name='perfil'),
    path('plantilla2.html/', plantilla2, name='plantilla2'),
    path('inicio2.html/', inicio2, name='inicio2'),
    path('premios2.html/', premios2, name='premios2'),
    path('recover.html/', recover, name='recover'),
    path('recuperar/', recuperar, name="recuperar"),
]
