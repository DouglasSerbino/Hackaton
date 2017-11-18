# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#Librerias para eliminar los documentos del servidor si es necesario
from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.db import models

# Create your models here.
class Documento(models.Model):
	nombre_documento = models.CharField(max_length=100, unique=True)
	descripcion = models.CharField(max_length=500)
	aprobacion = models.IntegerField(null=True, default='0')
	desaprobacion = models.IntegerField(null=True, default='0')
	archivo = models.FileField(upload_to='documentos/')

	class Meta:
		verbose_name='Documento'
		verbose_name_plural='Documentos'
	def __str__(self):
		return '%s' %(self.nombre_documento)

@receiver(post_delete, sender=Documento)
def archivo(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.archivo.delete(False)