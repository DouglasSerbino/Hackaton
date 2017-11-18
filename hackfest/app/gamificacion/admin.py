# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# importando modelos a utilizar
from .models import Puntaje, Logro, Nivel, Recompensa


# Register your models here.

# Configurando campos a mostrar para el Admin

# Registrando modelos

admin.site.register(Puntaje)
admin.site.register(Logro)
admin.site.register(Nivel)
admin.site.register(Recompensa)