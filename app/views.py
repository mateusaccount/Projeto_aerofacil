from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Viagem
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

class ViagemListView(LoginRequiredMixin, ListView):
    model = Viagem
    template_name = 'viagem_list.html'
    login_url = 'login'

class ViagemCreateView(LoginRequiredMixin, CreateView):
    model = Viagem
    fields = ['piloto', 'origem', 'destino', 'data_viagem', 'descricao']
    template_name = 'viagem_form.html'
    success_url = reverse_lazy('viagem_list')
    login_url = 'login'

class ViagemUpdateView(LoginRequiredMixin, UpdateView):
    model = Viagem
    fields = ['piloto', 'origem', 'destino', 'data_viagem', 'descricao']
    template_name = 'viagem_form.html'
    success_url = reverse_lazy('viagem_list')
    login_url = 'login'

class ViagemDeleteView(LoginRequiredMixin, DeleteView):
    model = Viagem
    template_name = 'viagem_confirm_delete.html'
    success_url = reverse_lazy('viagem_list')
    login_url = 'login'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automaticamente após o registro
            return redirect('viagem_list')  # Redireciona para a lista de viagens
        else:
            messages.error(request, "Erro ao cadastrar. Verifique os campos.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})