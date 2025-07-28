from django.db import models


# Create your models here.
class Estado(models.Model):
    nome = models.CharField(null=False,blank=False)
    uf = models.CharField(max_length=2,blank=False,null=False)

    class Meta():
        verbose_name_plural = 'Estados'
        
    def __str__(self):
        return f"{self.nome} ({self.uf})"

class Cidades(models.Model):
    nome = models.CharField(max_length=255,null=False,blank=False)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE,related_name='cidades')

    class Meta():
        verbose_name_plural = 'Cidades'

    
    def __str__(self):
        return f"{self.nome} ({self.estado.uf})"