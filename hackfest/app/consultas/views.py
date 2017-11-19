 	# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from models import Proyecto, Consulta
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def test(request):
	proyectos = Proyecto.objects.all()[:6]

	return render(request, 'consultas/test.html',{
		'proyectos':proyectos
		})


def ProyectosRecientes(request):
	proyectos = Proyecto.objects.all()[:6]

	return render(request, 'consultas/listarProyectos.html',{
		'proyectos':proyectos
		})

def CargarProyecto(request):
	# Se obtiene el proyecto del request
	ide = request.POST.get('proyecto')
	proyecto = Proyecto.objects.filter(id=ide)
	response = serializers.serialize("json",proyecto)
	return HttpResponse(response,content_type='application/json')

def VotacionProyecto(request):
	# obtenemos los parametros
	identificador = request.POST.get('proyecto')
	opcion = request.POST.get('opc')
	proyecto = Proyecto.objects.get(id=identificador)
	if opcion == '1':
		proyecto.dislike = proyecto.dislike + 1
		proyecto.save()
	else:
		proyecto.like = proyecto.like + 1
		proyecto.save()
	proyecto = Proyecto.objects.filter(id=identificador)
	response = serializers.serialize("json",proyecto)
	return HttpResponse(response,content_type='application/json')

def ComentarProyecto(request):
	ide = request.POST.get('proyecto')
	idUser = request.POST.get('user')
	comentario = request.POST.get('comentario')

	user = User.objects.get(id=idUser)
	proyecto = Proyecto.objects.get(id=ide)

	consulta = Consulta(comentario=comentario,usuario=user,proyecto=proyecto)
	consulta.save()
	return HttpResponse('ok')

def ListarComentarios(request):
	ide = request.POST.get('proyecto')
	proyecto = Proyecto.objects.get(id=ide)
	comentarios = Consulta.objects.filter(proyecto=proyecto)[:10]
	response = serializers.serialize("json",comentarios)
	return HttpResponse(response,content_type='application/json')