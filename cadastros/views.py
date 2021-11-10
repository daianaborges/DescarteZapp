from django.views.generic.edit import CreateView, UpdateView
from .models import Doadores, Doacao
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import TemplateView


class FormCadastro(TemplateView):
    template_name = 'cadastrar/form.html'


class DoadoresCreate(CreateView):
    model = Doadores
    fields = ['nome', 'sobrenome', 'dataNascimento', 'endereco', 'numero', 'bairro', 'cidade', 'telefonefixo',
              'celular']
    template_name = 'cadastrar/form.html'
    success_url = reverse_lazy('home')


class DoacaoCreate(CreateView):
    model = Doacao
    fields = ['quantidade', 'descricao', 'd_celular']
    template_name = 'cadastrar/form.html'
    success_url = reverse_lazy('inicio')

#################### UPDATE ########################

class DoadoresUpdate(UpdateView):
    model = Doadores
    fields = ['nome', 'sobrenome', 'dataNascimento', 'endereco', 'numero', 'bairro', 'cidade', 'telefonefixo',
              'celular']
    template_name = 'form.html'
    success_url = reverse_lazy('home.html')

#################### LISTA ########################

class DoadoresList(ListView):
    model = Doadores
    template_name = 'listas/doadores.html'
    
