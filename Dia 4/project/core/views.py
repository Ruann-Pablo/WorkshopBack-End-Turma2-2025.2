from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Endereco
from .form import EnderecoForm
import requests

class ViaCepFormView(FormView):
    template_name = 'viacep/endereco_form.html'
    form_class = EnderecoForm
    success_url = reverse_lazy('cep_list')

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


# CRUD completo
class CepList(ListView):
    model = Endereco
    template_name = 'viacep/viacep_list.html'
    context_object_name = 'enderecos'

class CepDetails(DetailView):
    model = Endereco
    template_name = 'viacep/viacep_details.html'
    context_object_name = 'endereco'

class CepUpdate(UpdateView):
    model = Endereco
    fields = ['cep', 'rua', 'bairro', 'cidade', 'estado']
    template_name = 'viacep/viacep_update.html'
    success_url = reverse_lazy('cep_list')
    context_object_name = 'endereco'

class CepDelete(DeleteView):
    model = Endereco
    template_name = 'viacep/viacep_delete.html'
    success_url = reverse_lazy('cep_list')
    context_object_name = 'endereco'
