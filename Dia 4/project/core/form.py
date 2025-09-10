from django import forms
from django.forms import ModelForm
from .models import Endereco

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep']
        labels = {
            'cep': 'CEP'
        }
        widget = {
            'cep':forms.TextInput(attrs={'placeholder': 'Digite o CEP'})
        }