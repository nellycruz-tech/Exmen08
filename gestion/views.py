from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Departamento, Empleado
from .forms import DepartamentoForm, EmpleadoForm

# ------------------ Departamentos ------------------
class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'gestion/departamento_list.html'
    context_object_name = 'departamentos'

class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = 'gestion/departamento_detail.html'

class DepartamentoCreateView(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'gestion/departamento_form.html'
    success_url = reverse_lazy('departamento_list')

class DepartamentoUpdateView(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'gestion/departamento_form.html'
    success_url = reverse_lazy('departamento_list')

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = 'gestion/departamento_confirm_delete.html'
    success_url = reverse_lazy('departamento_list')

# ------------------ Empleados ------------------
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'gestion/empleado_list.html'
    context_object_name = 'empleados'

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'gestion/empleado_detail.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'gestion/empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'gestion/empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'gestion/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')