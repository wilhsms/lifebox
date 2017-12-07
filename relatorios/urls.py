# -*- coding: utf-8 -*-
from django.conf.urls import url
from relatorios import views


urlpatterns = [
    url(r'', views.relatorios, name='exibir_relatorios'),
]
