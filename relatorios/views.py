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
    #Selecr * from Caixas
    if request.method == "POST":

        caixa_filtro=request.POST.get("caixa")
        equipamento_filtro=request.POST.get("equipamento")
        hospital_saida_filtro=request.POST.get("hospital_saida")
        hospital_chegada_filtro=request.POST.get("hospital_chegada")

        # query = Caixa.objects.filter(Caixa__idCaixa="CX000")

        #para retornar todo o banco caso algum campo vazio.
        #resultado = ""
        #if caixa_filtro == "" and equipamento_filtro == ""  and ...:
            #resultado = Viagem.Objects.all()

        #realizando o filtro utilizando o ou para valores nulos serem aceitos
        resultado = Viagem.objects.filter(Q(caixa__id=caixa_filtro) |
                                         Q(equipamento__id=equipamento_filtro) |
                                         Q(localPartida__id=hospital_saida_filtro) |
                                         Q(localChegada__id=hospital_chegada_filtro))


        #equipamento=equipamento_filtro,
        #localChegada=hospital_chegada_filtro,
        #localPartida=hospital_saida_filtro)
        print(resultado)

    caixas = Caixa.objects.all()
    equipamentos = Equipamento.objects.all()
    hospitais = Hospital.objects.all()
    return render(request, 'report.html', {'caixas' : caixas , 'equipamentos':equipamentos, 'hospitais':hospitais})
