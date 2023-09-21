from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class logueo(LoginView):
    template_name = 'paginas/logueo.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('inicio')

def inicio(request):
    return render (request, 'paginas/inicio.html')

def nosotros(request):
    return render (request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render (request, 'libros/index.html', {'libros':libros})




class CrearLibro(LoginRequiredMixin, CreateView):
    model = Libro
    fields = ['titulo','imagen','descripcion']
    success_url = reverse_lazy('libros')
    template_name = 'libros/crear-libro.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CrearLibro, self).form_valid(form)
    




def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render (request, 'libros/editar-libro.html', {'formulario':formulario})

def eliminar (request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')



