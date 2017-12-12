# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, status, generics
from rest_framework.decorators import detail_route, list_route, api_view
from rest_framework.response import Response
from datetime import datetime
from decimal import Decimal

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

class ViagemCompletoAtivasViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.filter(status = 3)
    serializer_class = ViagemFullSerializer

class ViagemCompletoViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemFullSerializer

class DetalheViewSet(viewsets.ModelViewSet):
    queryset = Detalhe.objects.all()
    serializer_class = DetalheSerializer


@api_view(['GET'])
def get_insere(request):
    '''Api temporária para recebimento de dados do arduino no formato atualmente utilizado pela equipe de engenharia.'''

    if request.query_params.get('content'):
        content = request.query_params['content']
        if content:
            array = content.split('/')

            #Formatar imeiEquipamento para o formato do sistema:
            inicio = array[0][:5]
            fim = array[0][10:]
            meio = (array[0][5:])[:5]

            imei = ".".join((inicio, meio, fim))

            #formatar data:
            try:
                data = datetime.strptime(array[9], "%Y-%m-%d %H:%M:%S")
            except ValueError:
                data = datetime.strptime(array[9], "%Y-%m-%d")

            detalhe = Detalhe.criar(
                imei,# Imei do Equipamento
                Decimal(array[1]),# Temperatura interna
                Decimal(array[2]),# Temperatura externa
                eval(array[3]),# virou
                eval(array[4]),# tombou
                Decimal(array[5]),# latitude
                Decimal(array[6]),# longitude
                Decimal(array[7]),# elevacao
                Decimal(array[8]),# velocidade
                data,# data_hora
                )

            #busca o equipamento associado:
            equipamento = Equipamento.objects.filter(imeiEquipamento = imei).first()

            #busca uma viagem em andamento com o equipamento encontrado
            viagem = Viagem.objects.filter(status = 3, equipamento = equipamento).first()

            if equipamento:
                detalhe.equipamento = equipamento

            if viagem:
                detalhe.viagem = viagem

            detalhe.save(force_insert=True)

            return Response("OK", status=status.HTTP_200_OK);

    return Response(status=status.HTTP_404_NOT_FOUND);
