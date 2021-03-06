# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Proyecto(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=500)
	presupuesto = models.DecimalField(max_digits = 10, decimal_places=2)
	gasto = models.DecimalField(max_digits = 10, decimal_places=2)
	fondos = models.DecimalField(max_digits = 10, decimal_places=2)
	like = models.IntegerField()
	dislike = models.IntegerField() 
	funcionario = models.ForeignKey(User)
	

class Consulta(models.Model):
	comentario = models.CharField(max_length=144)
	proyecto = models.ForeignKey(Proyecto)
	usuario  = models.ForeignKey(User)

	