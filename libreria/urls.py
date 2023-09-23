from django.urls import path
from . import views
from .views import (Eliminar,Editar,logueo, CrearLibro, RegistroUsuario, Nosotros, Inicio, Libros)
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', Inicio.as_view(), name="inicio"),
    path('nosotros/', Nosotros.as_view(), name="nosotros"),
    path('libros/', Libros.as_view(), name="libros"),
    path('libros/crear/', CrearLibro.as_view(), name="crear"),
    path('libros/editar/<int:pk>/', Editar.as_view(), name="editar-libro"),
    path('libros/eliminar/<int:pk>/', Eliminar.as_view(), name="eliminar"),
    path('logueo/', logueo.as_view(), name="logueo"),
    path('logout/', LogoutView.as_view(next_page='logueo'), name='logout'),
    path('registro/', RegistroUsuario.as_view(), name="registro-usuario"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


