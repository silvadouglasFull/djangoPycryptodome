# api/urls.py

from django.urls import path
from .views import HelloWorldView
from .views_consulta_cpf import ConsultaCPFView

urlpatterns = [
    path("hello/", HelloWorldView.as_view(), name="hello_world"),
    path("consulta/cpf/master/", ConsultaCPFView.as_view(), name="consulta_cpf"),
]
