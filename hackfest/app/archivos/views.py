# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
#Importacion del formulario creado y el modelo a usar
from forms import DocumentoForm
from models import Documento

from app.gamificacion.models import User

from django.http import HttpResponse
from django.db.models import F
from django.core import serializers


# Create your views here.
# VISTAS PARA LA PARTE ADMINISTRATIVA

#Funcion que retorna un formulario para el registro de documentos 
def documentos(request):
	documento = Documento.objects.all()
	if request.method == 'POST':
		form = DocumentoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return render(request, "Administracion/documentos.html", {'form':form, 'documento':documento})
	else:
		form = DocumentoForm()
	return render(request, "Administracion/documentos.html", {'form':form, 'documento':documento})

#Funcion que captura un objeto de tipo documento creado en la base de datos para posteriormente poder ser actualizado
def editardocs(request, id_documento):
	documento = get_object_or_404(Documento, id=id_documento)
	form = DocumentoForm(request.POST or None, request.FILES or None, instance=documento)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('archivos:principal'))
	return render(request, 'Administracion/editdocs.html', {'form': form}) 

#Funcion que permite la eliminacion de un objeto de tipo documento cuando se es requerido
def deletedocs(request):
	if request.method == 'POST':
		idd = request.POST.get('idd')
		documento = get_object_or_404(Documento, id=idd).delete()
	return HttpResponse(idd)


#VISTAS PARTE PUBLICA

#Funcion que representa la pagina de inicio de toda la plataforma
def inicio(request):
	return render(request,'Publico/inicio.html',{})

#Funcion que retorna los documentos agregados por el administrador 
#Esta funcion permite que los documentos agredados sean visibles para los usuarios en general
def documentacion(request):
	documento = Documento.objects.all()
	return render(request,'Publico/documentacion.html', {'documentos':documento})

#Funcion de puntuacion, permite que por medio de Ajax se envien valores de puntuacion de la informacion con el fin de saber si es util o no
def puntuar(request):
	if request.method == 'POST':
		if request.POST.get('util'):
			util = request.POST.get('util')
			like = Documento.objects.filter(id=util).update(aprobacion=F('aprobacion')+1)
			documento = Documento.objects.filter(id=util)
			response = serializers.serialize("json",documento)
			return HttpResponse(response,content_type='application/json')
			
		else:
			noutil = request.POST.get('noutil')
			dislike = Documento.objects.filter(id=noutil).update(desaprobacion=F('desaprobacion')+1)
			documento = Documento.objects.filter(id=noutil)
			response = serializers.serialize("json",documento)
			return HttpResponse(response,content_type='application/json')

	pass
	

