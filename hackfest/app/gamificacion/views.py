# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Importando al modelo User de Django
from django.contrib.auth.models import User
# Importando modelos de la app gamificacion
from app.gamificacion.models import *

# Create your views here.

# Vista: Principal
# Objetivo: Brindar la informacion del usuario y su avance en la aplicacion web
# Autor: Kendal Sosa (kendalalfonso37)
def principal(request):
	if request.user.is_authenticated():
		user = request.user
		perfil = PerfilUsuario.objects.filter(usuario__username = request.user)

	return render(request, 'Gamificacion/principal.html', {'perfil':perfil})