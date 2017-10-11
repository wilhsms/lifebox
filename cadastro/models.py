# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

OPERADORA_CHOICES = (
    ('Vivo', 'Vivo'),
    ('Oi', 'Oi'),
    ('Tim', 'Tim'),
    ('Claro', 'Claro'),
    ('Nextel', 'Nextel'),
)

class Equipamento(models.Model):
    nome = models.CharField(max_length=4)
    imeiEquipamento = models.CharField('IMEI', max_length=15)
    telefone = models.CharField(max_length=15)
    operadora = models.CharField(max_length=16, choices=OPERADORA_CHOICES)
    imeiSimCard = models.CharField('IMEI SIM Card', max_length=22)
    cor = models.CharField(max_length=7, null=True)
    caixa = models.ForeignKey(
        'Caixa', blank=True, null=True,
    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.imeiSimCard

class Caixa(models.Model):
    idCaixa= models.CharField('Identificação da Caixa', max_length=250)
    corCaixa= models.CharField('Cor da Tarja', max_length=250)
    informacaoAdicional= models.TextField('Informações Adicionais')

    def publish(self):
        self.save()

    def __str__(self):
        return self.idCaixa