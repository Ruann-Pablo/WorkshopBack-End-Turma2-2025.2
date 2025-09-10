from django.urls import path
from .views import ViaCepFormView, CepList, CepDetails, CepUpdate, CepDelete

urlpatterns = [
    path('', ViaCepFormView.as_view(), name='index'),
    path('list/', CepList.as_view(), name='cep_list'),
    path('detail/<int:pk>/', CepDetails.as_view(), name='cep_detail'),
    path('update/<int:pk>/', CepUpdate.as_view(), name='cep_update'),
    path('delete/<int:pk>/', CepDelete.as_view(), name='cep_delete'),
]
