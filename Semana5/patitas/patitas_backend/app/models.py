from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.

class Mascotas(models.Model):
       
    DISPONIBLE='DISPONIBLE'
    NO_DISPONIBLE='NO DISPONIBLE'
    
    STATUS_CHOISE= (
        (DISPONIBLE,'DISPONIBLE'),
        (NO_DISPONIBLE,'NO DISPONIBLE')
    )
    HEMBRA='HEMBRA'
    MACHO='MACHO'
    
    SEX_CHOISE= (
        (HEMBRA,'HEMBRA'),
        (MACHO,'MACHO')
    )
    
    MEDIO='MEDIO'
    ALTO='ALTO'
    BAJO='BAJO'
    
    ACTIVITY_CHOISE= (
        (ALTO,'ALTO'),
        (MEDIO,'MEDIO'),
        (BAJO,'BAJO')
    )
    LARGO='LARGO'
    CORTO='CORTO'
    
    HAIR_CHOISE= (
        (CORTO,'CORTO'),
        (LARGO,'LARGO')
    )
    MEDIANO='MEDIANO'
    PEQUEÑO='PEQUEÑO'
    GRANDE='GRANDE'
    
    TALL_CHOISE= (
        (PEQUEÑO,'PEQUEÑO'),
        (MEDIANO,'MEDIANO'),
        (GRANDE,'GRANDE')
    )
    mascota_id=models.AutoField(primary_key=True)
    mascota_nom=models.CharField(max_length=100,verbose_name='Nombre')
    mascota_est=models.CharField(max_length=20,choices=STATUS_CHOISE,verbose_name='Estado')
    mascota_img=CloudinaryField('Imagen',default='')
    mascota_age=models.IntegerField(default=0,verbose_name='Edad')
    mascota_sex=models.CharField(max_length=10,choices=SEX_CHOISE,verbose_name='Sexo')
    mascota_act=models.CharField(max_length=10,choices=ACTIVITY_CHOISE,verbose_name='Nivel de Actividad')
    mascota_hair=models.CharField(max_length=10,choices=HAIR_CHOISE,verbose_name='Pelo')
    mascota_tall=models.CharField(max_length=10,choices=TALL_CHOISE,verbose_name='Tamaño')
    mascota_hty=models.TextField(verbose_name='Historia')
    def __str__(self):
        return self.mascota_nom