from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.conf import settings

###################################################################################################
# modolo de monitoramento
@login_required
def relatorios(request):
    return render(request, 'report.html')
