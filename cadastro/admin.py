# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Equipamento, Caixa, Hospital, Viagem

admin.site.register({Equipamento, Caixa, Hospital, Viagem})
