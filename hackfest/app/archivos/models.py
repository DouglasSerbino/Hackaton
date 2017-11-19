# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#Librerias para eliminar los documentos del servidor si es necesario
from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.db import models

# Create your models here.
# Modelo: Documento
# Objetivo: clase de las que se mapean los atributos (campos) de la Tabla documento en la base de datos
# Autor: Douglas Serbino (douglasserbino)
class Documento(models.Model):
	nombre_documento = models.CharField(max_length=100, unique=True)
	descripcion = models.CharField(max_length=500)
	aprobacion = models.IntegerField(null=True, default='0')
	desaprobacion = models.IntegerField(null=True, default='0')
	archivo = models.FileField(upload_to='documentos/')
	
#Funcion que genera un nombre de espacio para determinados modelos
	class Meta:
		verbose_name='Documento'
		verbose_name_plural='Documentos'
	def __str__(self):
		return '%s' %(self.nombre_documento)

# Funcion que permite eliminar del servidor los archivos luego de ejecutar la accion de borrado en la vista del usuario
@receiver(post_delete, sender=Documento)
def archivo(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.archivo.delete(False)