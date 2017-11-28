# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from core.models import Viagem, Detalhe, Equipamento
from .serializers import UserSerializer, ViagemSingleSerializer, ViagemFullSerializer, DetalheSerializer, EquipamentoSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

class ViagemViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSingleSerializer

class DetalheViewSet(viewsets.ModelViewSet):
    queryset = Detalhe.objects.all()
    serializer_class = DetalheSerializer
    
class ViagemAtivasViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.filter(status = 3)
    serializer_class = ViagemFullSerializer