from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import TemplateView


# Create your views here.
class logueo(LoginView):
    template_name = 'paginas/logueo.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('libros')

class RegistroUsuario(FormView):
    template_name = 'paginas/registro_usuario.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(RegistroUsuario, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('inicio')
        return super(RegistroUsuario, self).get(*args, **kwargs)

class Inicio(TemplateView):
    template_name = ( 'paginas/inicio.html')

class Nosotros(TemplateView):
    template_name = ('paginas/nosotros.html')

class Libros( LoginRequiredMixin, TemplateView):
    template_name = ( 'libros/index.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = Libro.objects.all()
        return context



class CrearLibro(LoginRequiredMixin, CreateView):
    model = Libro
    fields = ['titulo','imagen','descripcion', 'pdf']
    success_url = reverse_lazy('libros')
    template_name = 'libros/crear-libro.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CrearLibro, self).form_valid(form)

class Editar(LoginRequiredMixin, UpdateView):
    model = Libro
    fields = ['titulo','imagen','descripcion', 'pdf']
    success_url = reverse_lazy('libros')
    template_name = 'libros/editar-libro.html'

class Eliminar(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = 'libros/eliminar-libro.html'
    success_url = reverse_lazy('libros')

