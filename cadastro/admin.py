from __future__ import unicode_literals
from django.contrib import admin
from .models import Equipamento
from .models import Caixa
#from .models import Hospital
#from .models import Viagem

admin.site.register(Equipamento)
admin.site.register(Caixa)
#admin.site.register(Hospital)
#admin.site.register(Viagem)
