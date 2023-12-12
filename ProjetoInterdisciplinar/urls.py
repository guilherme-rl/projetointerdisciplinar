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
    path('modalcliente/', views.ModalCliente, name='ModalCliente'),
    path('salvarcliente/', views.SalvarCliente, name='SalvarCliente'),
    path('modaldetalhescliente/', views.ModalDetalhesCliente, name='ModalDetalhesCliente'),
    path('modalexcluircliente/', views.ModalExcluirCliente, name='ModalExcluirCliente'),
    path('excluircliente/', views.ExcluirCliente, name='ExcluirCliente'),
    path('tabelaclientes/', views.TabelaClientes, name='TabelaClientes'),

    path('prestador/', views.IndexPrestador, name='Prestador'),
    path('modalnovoprestador/', views.ModalNovoPrestador, name='ModalNovoPrestador'),
    path('modalexcluirprestador/', views.ModalExcluirPrestador, name='ModalExcluirPrestador'),
    path('modaldetalhesprestador/', views.ModalDetalhesPrestador, name='ModalDetalhesPrestador'),
    path('excluirprestador/', views.ExcluirPrestador, name='ExcluirPrestador'),
    path('salvarprestador/', views.SalvarPrestador, name='SalvarPrestador'),
    path('tabelaprestadores/', views.TabelaPrestadores, name='TabelaPrestadores'),

    path('usuario/', views.IndexUsuario, name='Usuario'),
    path('modalnovousuario/', views.ModalNovoUsuario, name='ModalNovoUsuario'),
    path('novousuario/', views.NovoUsuario, name='NovoUsuario'),

    path('itemlocacao/', views.IndexItemLocacao, name='ItemLocacao'),
    path('modalnovoitemlocacao/', views.ModalNovoItemLocacao, name='ModalNovoItemLocacao'),
    path('modalexcluiritemlocacao/', views.ModalExcluirItemLocacao, name='ModalExcluirItemLocacao'),
    path('salvaritemlocacao/', views.SalvarItemLocacao, name='SalvarItemLocacao'),
    path('excluiritemlocacao/', views.ExcluirItemLocacao, name='ExcluirItemLocacao'),
    path('tabelaitenslocacao/', views.TabelaItensLocacao, name='TabelaItensLocacao'),


    path('unidademedida/', views.IndexUnidadeMedida, name='UnidadeMedida'),
    path('tabelaunidademedida/', views.TabelaUnidadeMedida, name='TabelaUnidadeMedida'),
    path('modalunidademedida/', views.ModalUnidadeMedida, name='ModalUnidadeMedida'),
    path('modalexcluirunidademedida/', views.ModalExcluirUnidadeMedida, name='ModalExcluirUnidadeMedida'),
    path('salvarunidademedida/', views.SalvarUnidadeMedida, name='SalvarUnidadeMedida'),
    path('excluirunidademedida/', views.ExcluirUnidadeMedida, name='ExcluirUnidadeMedida'),

    path('ingrediente/', views.IndexIngrediente, name='Ingrediente'),
    path('tabelaingrediente/', views.TabelaIngrediente, name='TabelaIngrediente'),
    path('modalingrediente/', views.ModalIngrediente, name='ModalIngrediente'),
    path('modalexcluiringrediente/', views.ModalExcluirIngrediente, name='ModalExcluirIngrediente'),
    path('excluiringrediente/', views.ExcluirIngrediente, name='ExcluirIngrediente'),
    path('salvaringrediente/', views.SalvarIngrediente, name='SalvarIngrediente'),

    path('prato/', views.IndexPrato, name='Prato'),
    path('tabelaprato/', views.TabelaPrato, name='TabelaPrato'),
    path('modalprato/', views.ModalPrato, name='ModalPrato'),
    path('modalexcluirprato/', views.ModalExcluirPrato, name='ModalExcluirPrato'),
    path('excluirprato/', views.ExcluirPrato, name='ExcluirPrato'),
    path('salvarprato/', views.SalvarPrato, name='SalvarPrato'),
    path('adicionaringredienteprato/', views.AdicionarIngredientePrato, name='AdicionarIngredientePrato'),

    path('orcamento/', views.IndexOrcamento, name='Orcamento'),
    path('tabelaorcamento/', views.TabelaOrcamento, name='TabelaOrcamento'),
    path('modalorcamento/', views.ModalOrcamento, name='ModalOrcamento'),
    path('modalexcluirorcamento/', views.ModalExcluirOrcamento, name='ModalExcluirOrcamento'),
    path('salvarorcamento/', views.SalvarOrcamento, name='SalvarOrcamento'),
    path('excluirorcamento/', views.ExcluirOrcamento, name='ExcluirOrcamento'),
    path('adicionarpratoorcamento/', views.AdicionarPratoOrcamento, name='AdicionarPratoOrcamento'),
    path('atualizarlistaingredientes/', views.AtualizarListaIngredientes, name='AtualizarListaIngredientes'),

    path('relatorio/', views.IndexRelatorio, name='Relatorio'),
    path('modalnovorelatorio/', views.ModalNovoRelatorio, name='ModalNovoRelatorio'),
    path('novorelatorio/', views.NovoRelatorio, name='NovoRelatorio'),

    path('contrato/', views.IndexContrato, name='Contrato'),
    path('modalnovocontrato/', views.ModalNovoContrato, name='ModalNovoContrato'),
    path('novocontrato/', views.NovoContrato, name='NovoContrato'),
    
    path('buscarentidadeporcpf/', views.BuscarEntidadePorCpf, name='BuscarEntidadePorCpf'),
    path('verificaentidade/', views.VerificaEntidadeExistente, name='VerificaEntidade'),
]
