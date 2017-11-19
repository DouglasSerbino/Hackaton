# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Importando el Modelo User para efectuar relaciones con este
from django.contrib.auth.models import User #, AbstractUser

# Create your models here.

# Modelo: Puntaje

# Modelo: Nivel
# Objetivo: Determinar el nivel al que pertenece un usuario
# Autor: Kendal Sosa (kendalalfonso37)
class Nivel(models.Model):
	titulo = models.CharField(max_length=35)
	descripcion = models.CharField(max_length=100)	
	sig_nivel = models.IntegerField()

# Objetivo: Determinar el puntaje del Usuario
# Autor: Kendal Sosa (kendalalfonso37)
class Puntaje(models.Model):
	valor = models.IntegerField()
	nivel = models.OneToOneField(Nivel, blank=True, null=True)
	

# Modelo: Recompensa
# Objetivo: Describir recompensas que tendra el usuario de acuerdo a su puntaje obtenido
# Autor: Kendal Sosa (kendalalfonso37)
class Recompensa(models.Model):
	titulo = models.CharField(max_length=35)
	descripcion = models.CharField(max_length=100)
	
	

# Modelo: Logro
# Objetivo: Describir los logros que ha obtenido el User
# Autor: Kendal Sosa (kendalalfonso37)
class Logro(models.Model):
	titulo = models.CharField(max_length=35)
	descripcion = models.CharField(max_length=100)
	recompensa = models.ForeignKey(Recompensa, blank=True, null=True, on_delete = models.CASCADE)


# Modelo: PerfilUsuario
# Objetivo: Registrar los datos que posee un usuario a manera de resumen 
# Autor: Kendal Sosa (kendalalfonso37)
class PerfilUsuario(models.Model):
	usuario = models.OneToOneField(User)
	nivel = models.OneToOneField(Nivel, blank=True, null=True)
	puntaje = models.OneToOneField(Puntaje, blank=True, null=True)
	logros = models.ForeignKey(Logro, blank=True, null=True)
