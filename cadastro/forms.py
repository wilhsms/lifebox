from django import forms
from django.forms.widgets import TextInput
from .models import Equipamento, Caixa

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