# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Equipamento(models.Model):
    nome = models.CharField(max_length=04)
    imeiEquipamento = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    operadora = models.CharField(max_length=16)
    imeiSimCard = models.CharField(max_length=22)


    def publish(self):
        #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.imeiSimCard
