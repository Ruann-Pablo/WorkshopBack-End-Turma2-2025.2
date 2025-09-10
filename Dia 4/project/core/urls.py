from django.urls import path
from . import views

urlpatterns = [
    path('consulta_cep/', views.consulta_cep, name='consulta_cep'),
    path('', views.endereco, name='endereco'),
]