# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput
from .models import Equipamento, Caixa, Hospital, Viagem

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ('nome', 'imeiEquipamento', 'telefone', 'operadora', 'imeiSimCard', 'cor', 'caixa')
        widgets = {
                   'cor': TextInput(attrs={'type': 'color'}),
                   }

class CaixaForm(forms.ModelForm):    
   class Meta:
       model = Caixa
       fields = ('idCaixa', 'corCaixa', 'informacaoAdicional')
       widgets = {
                   'corCaixa': TextInput(attrs={'type': 'color'}),
                   }

class HospitalForm(forms.ModelForm):    
   class Meta:
       model = Hospital
       fields = ('id', 'nome', 'telefone', 'nomeResponsavel', 'emailResponsavel', 'cep', 'logradouro', 'bairro', 'cidade', 'uf')
       widgets = {
           'id': TextInput(attrs={'readonly': 'True'}),
           'telefone': TextInput(attrs={'class': 'phone'}),
           'cep': TextInput(attrs={'autocomplete': 'off'}),
           'logradouro': TextInput(attrs={'autocomplete': 'off'}),
           'bairro': TextInput(attrs={'autocomplete': 'off'}),
           'cidade': TextInput(attrs={'autocomplete': 'off'}),
           'uf': TextInput(attrs={'autocomplete': 'off'}),

           }

class ViagemForm(forms.ModelForm):    
   class Meta:
       model = Viagem
       fields = ('localPartida', 'localChegada', 'caixa', 'equipamento')