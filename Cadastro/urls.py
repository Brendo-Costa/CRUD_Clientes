from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.ClienteListView.as_view(), name='cliente_listar'),
    path('criar/', views.ClienteCreateView.as_view(), name='cliente_criar'),
    path('alterar/<int:pk>', views.ClienteUpdateView.as_view(), name='cliente_alterar'),
    path('deletar/<int:pk>', views.ClienteDeleteView.as_view(), name='cliente_deletar'),
]