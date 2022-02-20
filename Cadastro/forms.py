from django import forms
from .models import Cliente
#from django.core.exceptions import ValidationError

# Criação do formulário para receber as entradas do usuário

class ClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente 
        fields = '__all__'