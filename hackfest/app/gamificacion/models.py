# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Importando el Modelo User para efectuar relaciones con este


# Create your models here.

# Modelo: Usuario
# Objetivo: Registrar los datos que posee un usuario a manera de resumen 
# Autor: Kendal Sosa (kendalalfonso37)
# Revisado por: Douglas Serbino (douglasserbino)

class Recompensa(models.Model):
 	titulo= models.CharField(max_length=200)
 	descripcion = models.CharField(max_length=300)

 	class Meta:
		verbose_name = "Recompensa"
		verbose_name_plural = "Recompensas"
		def __str__(self):
			return '%s' %(self.titulo)

class User(AbstractUser):
	nivel = models.IntegerField(null=True)
	puntuacion = models.IntegerField(null=True)
	recompensa = models.ForeignKey(Recompensa, null=True)

	