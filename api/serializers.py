# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Detalhe, Viagem, Hospital, Equipamento, Caixa

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CaixaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caixa
        fields = '__all__'

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class DetalheSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Detalhe
        fields = '__all__'
    
    def create(self, validated_data):
        #busca o equipamento associado:
        equipamento = Equipamento.objects.filter(imeiEquipamento = validated_data['imeiEquipamento']).first()
        
        #busca uma viagem em andamento com o equipamento encontrado
        viagem = Viagem.objects.filter(status = 3, equipamento = equipamento).first()
        
        if equipamento:
            validated_data['equipamento'] = equipamento
        
        if viagem:
            validated_data['viagem'] = viagem
            
        return Detalhe.objects.create(**validated_data)

class ViagemSerializer(serializers.ModelSerializer):
    detalhes = DetalheSerializer(many=True, read_only=True)
    caixa = CaixaSerializer(read_only=True)
    localPartida = HospitalSerializer(read_only=True)
    localChegada = HospitalSerializer(read_only=True)    

    class Meta:
        model = Viagem
        fields = '__all__'
        
class EquipamentoSerializer(serializers.ModelSerializer):
    detalhes = DetalheSerializer(many=True, read_only=True)
    
    class Meta:
        model = Equipamento
        fields = '__all__'
