# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Importando UserAdmin para Registrar Usuarios
from django.contrib.auth.admin import UserAdmin
# importando modelos a utilizar
from .models import Puntaje, Logro, Nivel, Recompensa, PerfilUsuario


# Register your models here.

# Registrando el modelo Usuario

# admin.site.register(Usuario, UserAdmin)


# Registrando los Demas modelos
admin.site.register(Puntaje)
admin.site.register(Logro)
admin.site.register(Nivel)
admin.site.register(Recompensa)
admin.site.register(PerfilUsuario)