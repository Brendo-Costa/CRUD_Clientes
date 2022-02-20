from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Cadastro.models import Cliente
from django.urls import reverse_lazy
from django.db.models import Q, Value
from django.db.models.functions import Concat
from datetime import timedelta, date

# Create your views here.

# Criação de todas as views usadas no projeto. Em todos, são usados classes, herdando de classes específicas do Django para cada aplicação.
# Classe Based Views - Listar, Deletar, Criar, Alterar são usadas no projeto. 
# Basicamente a view é a encarregada de abstrair a ação da página


# Lista 10 objetos e renderiza
class ClienteListView(ListView):
    template_name = 'Cadastro/cliente_list.html'
    model = Cliente
    queryset = Cliente.objects.order_by('nome')
    context_object_name = 'clientes'
    paginate_by = 10
    

# Busca objetos, e renderiza
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


# Busca os objetos criados até o último dia
class last1(ClienteListView):
    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        
        data_inicio = date.today()
        data_fim = (data_inicio - timedelta(days=1))
        
        queryset = queryset.filter(
            criado__range=(
                data_fim, data_inicio
            )
        )
        print(queryset)
        print(data_inicio)
        print(data_fim)

        return queryset


# Busca os objetos criados até os 7 últimos dias
class last7(ClienteListView):
    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        
        data_inicio = date.today()
        data_fim = (data_inicio - timedelta(days=7))       

        queryset = queryset.filter(
            criado__range=(
                data_fim, data_inicio
            )
        )

        return queryset


# Busca os objetos criados até os 30 últimos dias
class last30(ClienteListView):
    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        
        data_inicio = date.today()
        data_fim = (data_inicio - timedelta(days=30))

        queryset = queryset.filter(
            criado__range=(
                data_fim, data_inicio
            )
        )

        return queryset


# Busca os objetos criados até os 60 últimos dias
class last60(ClienteListView):
    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        
        data_inicio = date.today()
        data_fim = (data_inicio - timedelta(days=60))

        queryset = queryset.filter(
            criado__range=(
                data_fim, data_inicio
            )
        )

        return queryset


# Cria um novo objeto
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'Cadastro/cliente_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cliente_listar')


# Altera um objeto selecionado por ID
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'Cadastro/cliente_alterar.html'
    fields = '__all__'
    success_url = reverse_lazy('cliente_listar')


# Deleta um objeto selecionado por ID
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'Cadastro/excluir_elements.html'
    success_url = reverse_lazy('cliente_listar')

