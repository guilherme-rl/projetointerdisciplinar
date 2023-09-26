"""
ProjetoInterdisciplinar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from GestaoEvento import views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('contato/', views.Contato, name='Contato'),

    path('cliente/', views.IndexCliente, name='Cliente'),
    path('modalnovocliente/', views.ModalNovoCliente, name='ModalNovoCliente'),
    path('modalexcluircliente/', views.ModalExcluirCliente, name='ModalExcluirCliente'),
    path('salvarcliente/', views.SalvarCliente, name='SalvarCliente'),
    path('excluircliente/', views.ExcluirCliente, name='ExcluirCliente'),
    path('tabelaclientes/', views.TabelaClientes, name='TabelaClientes'),

    path('prestador/', views.IndexPrestador, name='Prestador'),
    path('modalnovoprestador/', views.ModalNovoPrestador, name='ModalNovoPrestador'),
    path('ModalExcluirPrestador/', views.ModalExcluirPrestador, name='ModalExcluirPrestador'),
    path('excluirprestador/', views.ExcluirPrestador, name='ExcluirPrestador'),
    path('salvarprestador/', views.SalvarPrestador, name='NovoPrestador'),
    path('tabelaprestador/', views.TabelaPrestador, name='TabelaPrestador'),

    path('usuario/', views.IndexUsuario, name='Usuario'),
    path('modalnovousuario/', views.ModalNovoUsuario, name='ModalNovoUsuario'),
    path('novousuario/', views.NovoUsuario, name='NovoUsuario'),

    path('itemlocacao/', views.IndexItemLocacao, name='ItemLocacao'),
    path('modalnovoitemlocacao/', views.ModalNovoItemLocacao, name='ModalNovoItemLocacao'),
    path('novoitemlocacao/', views.NovoItemLocacao, name='NovoItemLocacao'),

    path('unidademedida/', views.IndexUnidadeMedida, name='UnidadeMedida'),
    path('modalnovounidademedida/', views.ModalNovoUnidadeMedida, name='ModalNovoUnidadeMedida'),
    path('novounidademedida/', views.NovoUnidadeMedida, name='NovoUnidadeMedida'),

    path('ingrediente/', views.IndexIngrediente, name='Ingrediente'),
    path('modalnovoingrediente/', views.ModalNovoIngrediente, name='ModalNovoIngrediente'),
    path('novoingrediente/', views.NovoIngrediente, name='NovoIngrediente'),

    path('prato/', views.IndexPrato, name='Prato'),
    path('modalnovoprato/', views.ModalNovoPrato, name='ModalNovoPrato'),
    path('novoprato/', views.NovoPrato, name='NovoPrato'),

    path('orcamento/', views.IndexOrcamento, name='Orcamento'),
    path('modalnovoorcamento/', views.ModalNovoOrcamento, name='ModalNovoOrcamento'),
    path('novoorcamento/', views.NovoOrcamento, name='NovoOrcamento'),

    path('relatorio/', views.IndexRelatorio, name='Relatorio'),
    path('modalnovorelatorio/', views.ModalNovoRelatorio, name='ModalNovoRelatorio'),
    path('novorelatorio/', views.NovoRelatorio, name='NovoRelatorio'),

    path('contrato/', views.IndexContrato, name='Contrato'),
    path('modalnovocontrato/', views.ModalNovoContrato, name='ModalNovoContrato'),
    path('novocontrato/', views.NovoContrato, name='NovoContrato'),
]
