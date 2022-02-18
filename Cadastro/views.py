from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Cadastro.models import Cliente
from django.urls import reverse_lazy
from django.db.models import Q, Value
from django.db.models.functions import Concat
from datetime import timedelta, date

# Create your views here.

class ClienteListView(ListView):
    template_name = 'Cadastro/cliente_list.html'
    model = Cliente
    queryset = Cliente.objects.order_by('nome')
    context_object_name = 'clientes'
    

class Busca(ClienteListView):
    def get_queryset(self, *args, **kwargs):
        termo = self.request.GET.get('termo')
        campos = Concat('nome', Value(' '),'sobrenome')

        queryset = super().get_queryset(*args, **kwargs)

        if not termo:

            return queryset
        
        queryset = queryset.annotate(
            nome_completo = campos
        ).filter(
            Q(nome_completo__icontains=termo) |
            Q(nome__icontains=termo) |
            Q(sobrenome__icontains=termo) |
            Q(email__icontains=termo) |
            Q(cpf__icontains=termo) |
            Q(telefone__icontains=termo)
        )

        return queryset


class last1(ClienteListView):
    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        
        data_inicio = date.today()
        data_fim = (data_inicio - timedelta(days=1))

        queryset = queryset.filter(
            criado__range=(
                data_inicio, data_fim
            )
        )
        print(queryset)

        return queryset


class last7(ClienteListView):
    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        
        data_inicio = date.today()
        data_fim = (data_inicio - timedelta(days=7))       

        queryset = queryset.filter(
            criado__range=(
                data_inicio, data_fim
            )
        )

        return queryset


class last30(ClienteListView):
    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        
        data_inicio = date.today()
        data_fim = (data_inicio - timedelta(days=30))

        queryset = queryset.filter(
            criado__range=(
                data_inicio, data_fim
            )
        )

        return queryset


class last60(ClienteListView):
    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        
        data_inicio = date.today()
        data_fim = (data_inicio - timedelta(days=60))

        queryset = queryset.filter(
            criado__range=(
                data_inicio, data_fim
            )
        )

        return queryset


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'Cadastro/cliente_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cliente_listar')


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'Cadastro/cliente_alterar.html'
    fields = '__all__'
    success_url = reverse_lazy('cliente_listar')


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'Cadastro/excluir_elements.html'
    success_url = reverse_lazy('cliente_listar')

