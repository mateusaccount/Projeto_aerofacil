from django.db import models

class Viagem(models.Model):
    piloto = models.CharField(max_length=100, verbose_name="Nome do Piloto")
    origem = models.CharField(max_length=100, verbose_name="Origem")
    destino = models.CharField(max_length=100, verbose_name="Destino")
    data_viagem = models.DateField(verbose_name="Data da Viagem")
    descricao = models.TextField(blank=True, verbose_name="Descrição")

    def __str__(self):
        return f"{self.piloto} - {self.origem} para {self.destino} em {self.data_viagem}"
