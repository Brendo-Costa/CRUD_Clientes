from django import forms
from .models import Cliente
#from django.core.exceptions import ValidationError


class ClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente 
        fields = '__all__'