from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = ('nome', 'imeiEquipamento', 'telefone', 'operadora', 'imeiSimCard')
