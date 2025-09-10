from django.shortcuts import render
from .models import Endereco
from .form import EnderecoForm
import requests

# Create your views here.
def endereco(request):
    return render(request, 'endereco.html')

def consulta_cep(request):
    cep = request.GET.get('cep')

    if cep:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            data = response.json()
            endereco = Endereco(
                cep=data.get('cep'),
                rua=data.get('logradouro'),
                bairro=data.get('bairro'),
                cidade=data.get('localidade'),
                estado=data.get('uf'),
            )
            endereco.save()
            return render(request, 'consulta_cep.html', {'endereco': endereco, 'cep': cep})
        else:
            return render(request, 'consulta_cep.html', {'erro': 'não foi possível consultar o CEP'})
        
    return render(request, 'consulta_cep.html', {'mensagem': 'Nenhum cep enviado'})