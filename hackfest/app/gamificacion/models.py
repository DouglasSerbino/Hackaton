# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Importando el Modelo User para efectuar relaciones con este
from django.contrib.auth.models import User

# Create your models here.

# Modelo: Logro
# Objetivo: Describir los logros que ha obtenido el User
# Autor: Kendal Sosa (kendalalfonso37)
class Logro(models.Model):
	titulo = models.CharField(max_length=35)
	descripcion = models.CharField(max_length=100)
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)


# Modelo: Puntaje
# Objetivo: Determinar el puntaje del Usuario
# Autor: Kendal Sosa (kendalalfonso37)
class Puntaje(models.Model):
	valor = models.IntegerField()
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)

# Modelo: Nivel
# Objetivo: Determinar el nivel al que pertenece un usuario
# Autor: Kendal Sosa (kendalalfonso37)
class Nivel(models.Model):
	titulo = models.CharField(max_length=35)
	descripcion = models.CharField(max_length=100)
	usuario = models.OneToOneField(User, on_delete = models.CASCADE, blank=True)

# Modelo: Recompensa
# Objetivo: Describir recompensas que tendra el usuario de acuerdo a su puntaje obtenido
# Autor: Kendal Sosa (kendalalfonso37)
class Recompensa(models.Model):
	titulo = models.CharField(max_length=35)
	descripcion = models.CharField(max_length=100)
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)
