# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # carrega user para inserção no campo createdPor
import csv


###################################################################################################
# Banco Equipamento:
OPERADORA_CHOICES = (
    ('Vivo', 'Vivo'),
    ('Oi', 'Oi'),
    ('Tim', 'Tim'),
    ('Claro', 'Claro'),
    ('Nextel', 'Nextel'),
)

class Equipamento(models.Model):
    idEquipamento = models.CharField('Id Equipamento', max_length=6, unique=True)
    imeiEquipamento = models.CharField('IMEI do Equipamento', max_length=22, unique=True)
    telefone = models.CharField('Telefone', max_length=15)
    operadora = models.CharField('Operadora', max_length=8, choices=OPERADORA_CHOICES)
    imeiSimCard = models.CharField('IMEI SIM Card', max_length=26)
    createdEm = models.DateTimeField('Registro criado em:', default=timezone.now)
    createdPor = models.ForeignKey(User, default=User)

    def publish(self):
        self.save()
        self.idEquipamento = "EQ" + str(self.id).zfill(3)
        self.save()

    def __str__(self):
        return self.idEquipamento

###################################################################################################
# Banco Caixa:
class Caixa(models.Model):
    idCaixa = models.CharField('Id Caixa', max_length=6, unique=True)
    autorizacao = models.CharField('Autorização da Caixa', max_length=20, unique=True)
    corCaixa = models.CharField('Cor da Tarja', max_length=7, null=True)
    informacaoAdicional = models.TextField('Informações Adicionais', max_length=200)
    createdEm = models.DateTimeField('Registro criado em:', default=timezone.now)
    createdPor = models.ForeignKey(User, default=User)

    def publish(self):
        self.save()
        self.idCaixa = "CX" + str(self.id).zfill(3)
        self.save()

    def __str__(self):
        return self.idCaixa

###################################################################################################
# Banco Hospital:
class Hospital(models.Model):
    nome = models.CharField('Nome do Hospital', max_length=50)
    telefone = models.CharField('Telefone', max_length=15)
    nomeResponsavel = models.CharField('Responsável', max_length=30)
    emailResponsavel = models.CharField('E-mail', max_length=50)
    cep = models.CharField('CEP',max_length=10)
    logradouro = models.CharField('Endereço',max_length=50)
    bairro = models.CharField('Bairro',max_length=30)
    cidade = models.CharField('Cidade',max_length=30)
    uf = models.CharField('UF',max_length=2)
    createdEm = models.DateTimeField('Registro criado em:', default=timezone.now)
    createdPor = models.ForeignKey(User, default=User)


    def publish(self):
        self.save()

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return u'{f}'.format(f=self.nome)

    class Meta:
        verbose_name_plural = 'Hospitais'

###################################################################################################
# Banco Status:
class Status(models.Model):
    dscStatus = models.CharField('Descrição', max_length=50)
    codStatus = models.CharField('Código', max_length=2)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return u'{f}'.format(f=self.dscStatus)

    class Meta:
        verbose_name_plural = 'Status'
        verbose_name = 'Status'


###################################################################################################
STATUS_VIAGEM = (
    ('1', 'Em Elaboracao'),
    ('2', 'Aguardando Viagem'),
    ('3', 'Viagem Iniciada'),
    ('4', 'Viagem Finalizada'),
)

# Banco Viagem:
class Viagem(models.Model):
    localPartida = models.ForeignKey('Hospital', related_name='local_partida')
    localChegada = models.ForeignKey('Hospital', related_name='local_chegada')
    caixa = models.ForeignKey('Caixa')
    equipamento = models.ForeignKey('Equipamento')
    status = models.CharField('Status', max_length=2, choices=STATUS_VIAGEM)
    nomeTransportador = models.CharField('Transportado por', max_length=30, null=True, blank=True)
    contato = models.CharField('Contato', max_length=15, null=True, blank=True)
    obs = models.TextField('Observações', max_length=500, null=True, blank=True)
    createdEm = models.DateTimeField('Registro criado em:', default=timezone.now)
    createdPor = models.ForeignKey(User, default=User)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Viagens'
        verbose_name = 'Viagem'

###################################################################################################
# Banco Detalhe:
class Detalhe(models.Model):
    numLongitudeDeta = models.DecimalField('Longitude', max_digits=9, decimal_places=6)
    numLatitudeDeta = models.DecimalField('Latitude', max_digits=9, decimal_places=6)
    numTemperatura1Deta = models.DecimalField('Temperatura 1', max_digits=4, decimal_places=1, default=1)
    numTemperatura2Deta = models.DecimalField('Temperatura 2', max_digits=4, decimal_places=1, default=2)
    indVirouDeta = models.BooleanField('Virou?')
    indTombouDeta = models.BooleanField('Tombou?')
    imeiEquipamento = models.CharField('IMEI do Equipamento', max_length=22)
    viagem = models.ForeignKey('Viagem', related_name='detalhes', blank=True, null=True)
    equipamento = models.ForeignKey('Equipamento', related_name='detalhes', blank=True, null=True)

    def __str__(self):
        return str(self.imeiEquipamento)
    '''
    def saveCsv(self, path):
        records = csv.reader(path)
        records.readline()#ignora a primeira linha
        for record in records:
            self.numLongitudeDeta = record[0]
            self.numLatitudeDeta = record[1]
            self.numTemperatura1Deta = record[2]
            self.numTemperatura2Deta = record[3]
            self.indVirouDeta = record[4]
            self.indTombouDeta = record[5]
            self.imeiEquipamento = record[6]
            
            equipamento = Equipamento.objects.filter(imeiEquipamento = self.imeiEquipamento).first()
            viagem = Viagem.objects.filter(status = 3, equipamento = equipamento).first()
            
            if equipamento:
                self.equipamento = equipamento
            
            if viagem:
                self.viagem = viagem
            
            self.save()
    '''
    class Meta:
      verbose_name = u"Detalhe"
      verbose_name_plural = u"Detalhes"

###################################################################################################
# Banco importa: para importação e armazenamento de CSVs
class Importa(models.Model):
    imei = models.CharField('IMEI', max_length=22, unique=True)
    dia = models.DateField('Dia', max_length=10)
    hora = models.TimeField('Hora', max_length=8)
    longitude = models.IntegerField('Longitude')
    latitude = models.IntegerField('Latitude')
    altitude = models.IntegerField('Altitude')
    velocidade = models.DecimalField('Velocidade', max_digits=4, decimal_places=2)
    temperatura = models.DecimalField('Temperatura', max_digits=4, decimal_places=2)
    vibra = models.BooleanField('Vibrou?', )
    tombo = models.BooleanField('Tombou?', )
    course = models.IntegerField('Curso')
    satelites = models.SmallIntegerField('Satélites')
    createdEm = models.DateTimeField('Registro criado em:', default=timezone.now)
    createdPor = models.ForeignKey(User, default=User)


    def publish(self):
        self.save()

    def __str__(self):
        return self.imei

## exemplo para utilizar upload de arquivos
#   def user_directory_path(instance, filename):
#    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#    return 'user_{0}/{1}'.format(instance.user.id, filename)
#
#  class MyModel(models.Model):
#    upload = models.FileField(upload_to=user_directory_path)
#
