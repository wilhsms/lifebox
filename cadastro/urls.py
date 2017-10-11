from __future__ import unicode_literals
from django.conf.urls import url
from cadastro import views

urlpatterns = [
    url(r'^equipamento/$', views.equipamento_pesquisar, name='equipamento_pesquisar'),
    url(r'^equipamento/novo$', views.equipamento_criar, name='equipamento_criar'),
    url(r'^equipamento/(?P<pk>\d+)/$', views.equipamento_editar, name='equipamento_editar'),
    url(r'^caixa/$', views.caixa_pesquisar, name='caixa_pesquisar'),
    url(r'^caixa/novo$', views.caixa_criar, name='caixa_criar'),
    url(r'^caixa/(?P<pk>\d+)/$', views.caixa_editar, name='caixa_editar'),    
]
