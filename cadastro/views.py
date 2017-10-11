from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from cadastro.models import Equipamento, Caixa
from cadastro.forms import EquipamentoForm, CaixaForm

###################################################################################################
# Cadastro de Equipamentos:
@login_required
def equipamento_pesquisar(request):
    equipamentos = Equipamento.objects.all()
    return render(request,
                  'equipamento/pesquisa.html',
                  {'equipamentos': equipamentos})

@login_required
def equipamento_criar(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.save()
            return redirect('equipamento_pesquisar')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamento/formulario.html', {'form': form})

@login_required
def equipamento_editar(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == "POST":
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.save()
            return redirect('equipamento_pesquisar')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamento/formulario.html', {'form': form})


###################################################################################################
# Cadastro de Caixas:
@login_required
def caixa_pesquisar(request):
    caixas = Caixa.objects.all()
    return render(request, 'caixa/pesquisa.html', {'caixas': caixas})


@login_required
def caixa_criar(request):
    if request.method == 'POST':
        form = CaixaForm(request.POST)
        if form.is_valid():
            caixa = form.save(commit=False)
            caixa.save()
            return redirect('caixa_pesquisar')
    else:
        form = CaixaForm()
    return render(request, 'caixa/formulario.html', {'form': form})


@login_required
def caixa_editar(request, pk):
    caixa = get_object_or_404(Caixa, pk=pk)
    if request.method == "POST":
        form = CaixaForm(request.POST, instance=caixa)
        if form.is_valid():
            caixa = form.save(commit=False)
            caixa.save()
            return redirect('caixa_pesquisar')
    else:
        form = CaixaForm(instance=caixa)
    return render(request, 'caixa/formulario.html', {'form': form})

###################################################################################################
# Cadastro de Hospitais:

###################################################################################################
# Cadastro de Viagens:
