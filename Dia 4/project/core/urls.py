from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViaCepFormView.as_view(), name='index'),
    path('consulta_cep/', views.consulta_cep, name='consulta_cep'),
    path('endereco/', views.endereco, name='endereco'),
]