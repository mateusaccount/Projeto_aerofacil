from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
from .models import Viagem
from .forms import ViagemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

@login_required
def viagem_list(request):
    context = {
        "viagens": Viagem.objects.all()
    }
    return render(request, "viagem_list.html", context)

def viagem_detail(request, viagem_id):
    context = {
        "viagem": get_object_or_404(Viagem, pk=viagem_id)
    }
    return render(request, "viagem_detail.html", context)

@login_required
def viagem_create(request):
    if request.method == "POST":
        form = ViagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viagem_list')
    else:
        form = ViagemForm()
    return render(request, "viagem_form.html", {"form": form})

@login_required
def viagem_update(request, viagem_id):
    viagem = get_object_or_404(Viagem, pk=viagem_id)
    if request.method == "POST":
        form = ViagemForm(request.POST, instance=viagem)
        if form.is_valid():
            form.save()
            return redirect('viagem_list')
    else:
        form = ViagemForm(instance=viagem)
    return render(request, "viagem_form.html", {"form": form})

@login_required
def viagem_delete(request, viagem_id):
    viagem = get_object_or_404(Viagem, pk=viagem_id)
    if request.method == "POST":
        viagem.delete()
        return redirect('viagem_list')
    return render(request, "viagem_confirm_delete.html", {"viagem": viagem})

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('viagem_list')  # Redireciona para a página de lista de viagens
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos.'})
    
    return render(request, 'login.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout
