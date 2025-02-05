from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Viagem
from .forms import ViagemForm

# ------------------------
# Autenticação
# ------------------------
def base(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')  # Redireciona para a página de lista de viagens
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos.'})
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('base')  # Redireciona para a página de login após o logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('viagem_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# ------------------------
# CRUD das Viagens
# ------------------------

@login_required
def viagem_list(request):
    """Lista todas as viagens cadastradas"""
    viagens = Viagem.objects.all()
    return render(request, "viagem_list.html", {"object_list": viagens})

@login_required
def viagem_detail(request, pk):
    """Exibe detalhes de uma viagem específica"""
    viagem = get_object_or_404(Viagem, pk=pk)
    return render(request, "viagem_detail.html", {"viagem": viagem})

@login_required
def viagem_create(request):
    """Cria uma nova viagem"""
    if request.method == "POST":
        form = ViagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viagem_list')
    else:
        form = ViagemForm()
    return render(request, "viagem_form.html", {"form": form})

@login_required
def viagem_update(request, pk):
    """Atualiza uma viagem existente"""
    viagem = get_object_or_404(Viagem, pk=pk)
    if request.method == "POST":
        form = ViagemForm(request.POST, instance=viagem)
        if form.is_valid():
            form.save()
            return redirect('viagem_list')
    else:
        form = ViagemForm(instance=viagem)
    return render(request, "viagem_form.html", {"form": form})

@login_required
def viagem_delete(request, pk):
    """Deleta uma viagem existente"""
    viagem = get_object_or_404(Viagem, pk=pk)
    if request.method == "POST":
        viagem.delete()
        return redirect('viagem_list')
    return render(request, "viagem_confirm_delete.html", {"viagem": viagem})
