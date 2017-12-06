# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput, Textarea, DateTimeInput
from datetimewidget.widgets import DateTimeWidget
from .models import Equipamento, Caixa, Hospital, Viagem

###################################################################################################
# Formulário Equipamento:
class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ('idEquipamento', 'imeiEquipamento', 'telefone', 'operadora', 'imeiSimCard')
        widgets = {
            'id': TextInput(attrs={'readonly': 'True'}),
            'idEquipamento': TextInput(attrs={'class':'eq_mask', 'readonly': 'True', 'placeholder': ''}),
            'imeiEquipamento': TextInput(attrs={'class': 'imeiTracker'}),
            'telefone': TextInput(attrs={'class': 'phone'}),
            'imeiSimCard': TextInput(attrs={'class': 'imeiSimCard'}),
            }

###################################################################################################
# Formulário Caixa:
class CaixaForm(forms.ModelForm):
   class Meta:
       model = Caixa
       fields = ('idCaixa', 'autorizacao', 'corCaixa', 'informacaoAdicional')
       widgets = {
                'id': TextInput(attrs={'readonly': 'True'}),
                'idCaixa': TextInput(attrs={'class':'cx_mask', 'readonly': 'True', 'placeholder': ''}),
                'corCaixa': TextInput(attrs={'type': 'color'}),
                'informacaoAdicional': Textarea(attrs={'rows':'5', 'onkeyup':"mostrarResultado(this.value,200,'spcontando');contarCaracteres(this.value,200,'sprestante')"}),
                }

###################################################################################################
# Formulário Hospital:
class HospitalForm(forms.ModelForm):
   class Meta:
       model = Hospital
       fields = ('nome', 'telefone', 'nomeResponsavel', 'emailResponsavel', 'cep', 'logradouro', 'bairro', 'cidade', 'uf')
       widgets = {
           'id': TextInput(attrs={'readonly': 'True'}),
           'telefone': TextInput(attrs={'class': 'phone'}),
           'cep': TextInput(attrs={'class': 'cep'}),
           'logradouro': TextInput(attrs={'autocomplete': 'on'}),
           'bairro': TextInput(attrs={'autocomplete': 'on'}),
           'cidade': TextInput(attrs={'autocomplete': 'on'}),
           'uf': TextInput(attrs={'autocomplete': 'on'}),
           }


###################################################################################################
# Formulário Viagem:
class ViagemForm(forms.ModelForm):
    class Meta:
       model = Viagem
       fields = ('status', 'localPartida', 'localChegada', 'caixa', 'equipamento', 'nomeTransportador', 'contato', 'obs', 'dataInicio', 'dataFim')
       widgets = {
           'contato': TextInput(attrs={'class': 'phone'}),
           'obs': Textarea(attrs={'rows':'5', 'onkeyup':"mostrarResultado(this.value,500,'spcontando');contarCaracteres(this.value,500,'sprestante')"}),
           'dataInicio': DateTimeWidget(usel10n=True),
           'dataFim': DateTimeWidget(usel10n=True)
           }


class UploadFileForm(forms.Form):
    file = forms.FileField(label = '' , widget = forms.FileInput(attrs={'accept':"*.*", 'class':'custom-file-input'}))
