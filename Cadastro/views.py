from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Cadastro.models import Cliente
from django.urls import reverse_lazy

# Create your views here.

class ClienteListView(ListView):
    template_name = 'Cadastro/cliente_list.html'
    model = Cliente
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'Cadastro/cliente_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cliente_listar')


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'Cadastro/cliente_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cliente_listar')


class ClienteDeleteView(DeleteView):
    pass


