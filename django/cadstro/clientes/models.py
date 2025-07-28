from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField()
    email = models.EmailField()
    senha = models.CharField()

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nome} {self.email}'