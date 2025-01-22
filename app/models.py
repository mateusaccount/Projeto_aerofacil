from django import forms
from django.db import models
from django.contrib.auth.models import User

class Viagem(models.Model):
    piloto = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Nome do Piloto")
    origem = models.CharField(max_length=100, verbose_name="Origem")
    destino = models.CharField(max_length=100, verbose_name="Destino")
    data_viagem = models.DateField(verbose_name="Data da Viagem")
    descricao = models.TextField(blank=True, verbose_name="Descrição")

    def __str__(self):
        return f"{self.origem} para {self.destino} em {self.data_viagem}"

class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ['origem', 'destino', 'data_viagem', 'descricao']
