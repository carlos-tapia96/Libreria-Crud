from django.urls import path
from . import views
from .views import (logueo, CrearLibro)
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('libros/', views.libros, name="libros"),
    path('libros/crear/', CrearLibro.as_view(), name="crear"),
    path('libros/editar/', views.editar, name="editar"),
    path('libros/eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('libros/editar/<int:id>', views.editar, name="editar-libro"),
    path('logueo/', logueo.as_view(), name="logueo"),
    path('logout/', LogoutView.as_view(next_page='logueo'), name='logout')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


