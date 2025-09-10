from django.views.generic.edit import FormView
from django.shortcuts import render
from .models import Endereco
from .form import EnderecoForm
import requests

# Create your views here.
class ViaCepFormView(FormView):
    template_name = 'endereco.html'
    form_class = EnderecoForm
    success_url = '/endereco/'

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
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
            return super().form_valid(form)
        else:
            form.add_error('cep', 'Não foi possível consultar o CEP')
            return self.form_invalid(form)



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


class CepList():
    model = Endereco
    template_name = 'viacep/viacep_list.html'
    context_object_name = 'ListCep'

class CepDetails():
    model = Endereco
    template_name = 'viacep/viacep_details.html'
    context_object_name = 'DetailsCep'

class CepUpdate():
    model = Endereco
    template_name = 'viacep/viacep_update.html'
    context_objexct_name = 'UpdateCep'

class CepDelete():
    model = Endereco
    template_name = 'viacep/viacep_delete.html'
    context_object_name = 'DeleteCep'