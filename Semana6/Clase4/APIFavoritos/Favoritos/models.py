
from django.db import models

# Create your models here.

class Favorito(models.Model):
    favorito_id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=200,default='',verbose_name='TITULO')
    url=models.CharField(max_length=200,default='',verbose_name='URL')
    fecha=models.DateTimeField(auto_now_add=True,verbose_name='FECHA')
    
    def __str__(self):
        return self.titulo