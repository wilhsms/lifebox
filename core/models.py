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
        return self.nome

class Caixa(models.Model):
    idCaixa= models.CharField('Identificação da Caixa', max_length=250)
    corCaixa= models.CharField('Cor da Tarja', max_length=7, null=True)
    informacaoAdicional= models.TextField('Informações Adicionais')

    def publish(self):
        self.save()

    def __str__(self):
        return self.idCaixa

class Hospital(models.Model):
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=16)
    nomeResponsavel = models.CharField('Responsável', max_length=250)
    emailResponsavel = models.CharField('E-mail', max_length=250)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def publish(self):
        self.save()

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return u'{f}'.format(f=self.nome)

    class Meta:
        verbose_name_plural = 'Hospitais'

class Viagem(models.Model):
    localPartida = models.ForeignKey('Hospital', related_name='local_partida')
    localChegada = models.ForeignKey('Hospital', related_name='local_chegada')
    caixa = models.ForeignKey('Caixa')
    equipamento = models.ForeignKey('Equipamento')

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Viagens'
