# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
# Importando al modelo User de Django
from django.contrib.auth import login, authenticate
#from django.contrib.auth.models import User
# Importando modelos
from app.gamificacion.models import Recompensa
from django.contrib.auth import get_user_model
User = get_user_model()

from forms import SignUpForm
# Importando modelos de la app gamificacion

# Create your views here.
# Vista: Registro
# Objetivo: Brindar el registro del usuario y su avance en la aplicacion web
# Autor: Kendal Sosa (kendalalfonso37)
# Revisado por: Douglas Serbino (douglasserbino)
def registro(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'Usuarios/users.html', {'form': form})

# Vista: Perfil
# Objetivo: brindar la informacion del usuario y su avance
# Autor: Kendal Sosa (kendalalfonso37)
def perfil(request):

	return render(request, 'Gamificacion/principal.html')