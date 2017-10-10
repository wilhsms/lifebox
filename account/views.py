from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import UserRegistrationForm
from cadastro.models import Equipamento


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

#Funcoes adicionadas por Marcio Ribeiro em 05-out para chamar as paginas de:
#Monitorar Orgao
@login_required
def monitor(request):
    return render(request,
                  'account/monitor.html',
                  {'section': 'dashboard'})

#Emitir Relatorios
@login_required
def report(request):
    return render(request,
                  'account/report.html',
                  {'section': 'dashboard'})

#Gerenciar Cadastros
@login_required
def management(request):
    return render(request,
                  'account/management.html',
                  {'section': 'dashboard'})

#Gerenciar Cadastros
@login_required
def equipamento(request):
    equipamentos = Equipamento.objects.all()
    return render(request,
                  'account/equipamento.html',
                  {'equipamentos': equipamentos})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})
