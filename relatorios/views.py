from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.conf import settings
from core.models import *

###################################################################################################
# modolo de monitoramento
@login_required
def relatorios(request):
    resultado = None
    #Realiza o filtro em cada tabela
    if request.method == "POST":
        caixa_filtro=request.POST.get("caixa")
        equipamento_filtro=request.POST.get("equipamento")
        hospital_saida_filtro=request.POST.get("hospital_saida")
        hospital_chegada_filtro=request.POST.get("hospital_chegada")

        #Une os filtros realizando um filtro combinado entre todas as tabelas
        resultado = Viagem.objects.all()
        if caixa_filtro:
            resultado = resultado.filter(caixa__id=caixa_filtro)
        if equipamento_filtro:
            resultado = resultado.filter(equipamento__id=equipamento_filtro)
        if hospital_saida_filtro:
            resultado = resultado.filter(localPartida__id=hospital_saida_filtro)
        if hospital_chegada_filtro:
            resultado = resultado.filter(localChegada__id=hospital_chegada_filtro)
        #Print que mostra o resultado no terminal
        print(resultado)
    #Retorna as caixas e equipamentos para realizar filtro
    caixas = Caixa.objects.all()
    equipamentos = Equipamento.objects.all()
    hospitais = Hospital.objects.all()
    return render(request, 'report.html', {'caixas' : caixas , 'equipamentos' : equipamentos, 'hospitais' : hospitais, 'viagens': resultado})
