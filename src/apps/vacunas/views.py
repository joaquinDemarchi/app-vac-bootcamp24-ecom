from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import FormVacuna
from .models import Vacuna, Dosis


class Listar(ListView):
    template_name = 'vacunas/lista_new.html'
    model = Vacuna
    context_object_name = "vacunas"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        ctx = super(Listar, self).get_context_data(**kwargs)
        ctx["titulo"] = "LISTA DE VACUNAS"
        return ctx


class VacunaUpdate(UpdateView):
    model = Vacuna
    fields = ['codigo', 'nombre', 'ca_dosis']
    template_name = 'vacunas/editar_new.html'
    success_url = reverse_lazy('vacunas:lista')  # Redirigir a la lista de vacunas después de la edición
    pk_url_kwarg = "id_vacuna"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Vacuna'
        print("****************")
        print(self.kwargs["id_vacuna"])
        return context


class VacunaDetail(DetailView):
    model = Vacuna
    template_name = 'vacunas/detalle_new.html'
    context_object_name = 'vacuna'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dosis'] = Dosis.objects.filter(vacuna=self.object)
        return context


class VacunaDeleteView(DeleteView):
    model = Vacuna
    template_name = 'vacunas/confirmar_eliminacion_new.html'
    success_url = reverse_lazy('vacunas:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dosis'] = Dosis.objects.filter(vacuna=self.object)
        return context


class Nuevo(CreateView):
    template_name = 'vacunas/nuevo.html'
    model = Vacuna
    form_class = FormVacuna
    success_url = reverse_lazy("vacunas:lista")

    def get_context_data(self, **kwargs):
        ctx = super(Nuevo, self).get_context_data(**kwargs)
        return ctx
