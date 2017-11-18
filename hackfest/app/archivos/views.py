# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
#Importacion del formulario creado y el modelo a usar
from forms import DocumentoForm
from models import Documento


# Create your views here.
# VISTAS PARA LA PARTE ADMINISTRATIVA
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

def editardocs(request, id_documento):
	documento = get_object_or_404(Documento, id=id_documento)
	form = DocumentoForm(request.POST or None, request.FILES or None, instance=documento)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('archivos:principal'))
	return render(request, 'Administracion/editdocs.html', {'form': form}) 

def deletedocs(request, id_documento):
	documento = get_object_or_404(Documento, id=id_documento).delete()
	return response("Elemento eliminado")


#VISTAS PARTE PUBLICA
def inicio(request):
	return render(request,'Publico/inicio.html',{})

def documentacion(request):
	documento = Documento.objects.all()
	return render(request,'Publico/documentacion.html', {'documentos':documento})

