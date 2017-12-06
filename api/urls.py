# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework import routers
from api import apis


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'viagem/ativas', apis.ViagemCompletoAtivasViewSet)
router.register(r'equipamento', apis.EquipamentoViewSet)
router.register(r'detalhe', apis.DetalheViewSet)
router.register(r'viagem', apis.ViagemCompletoViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^get_insere/', apis.get_insere, name="get_insere"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
