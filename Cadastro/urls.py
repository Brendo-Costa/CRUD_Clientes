from django.urls import path
from . import views

# Criação de todas as rotas presentes no projeto. Onde representam o caminho referente a view que abstraia a ação em si que usuário
# deseja realizar.

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='cliente_listar'),
    path('criar/', views.ClienteCreateView.as_view(), name='cliente_criar'),
    path('alterar/<int:pk>', views.ClienteUpdateView.as_view(), name='cliente_alterar'),
    path('deletar/<int:pk>', views.ClienteDeleteView.as_view(), name='cliente_deletar'),
    path('busca/', views.Busca.as_view(), name='cliente_busca'),
    path('last1/', views.last1.as_view(), name='cliente_last1'),
    path('last7/', views.last7.as_view(), name='cliente_last7'),
    path('last30/', views.last30.as_view(), name='cliente_last30'),
    path('last60/', views.last60.as_view(), name='cliente_last60'),
]