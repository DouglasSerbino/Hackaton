from django.conf.urls import url
from django.contrib import admin
from app.archivos import views 
# Importando la vista basada en clases RedirectView para redirigir a /administracion/index
from django.views.generic import RedirectView

urlpatterns = [
 url(r'^puntuar/', views.puntuar, name='puntuar'),
 url(r'^$', RedirectView.as_view(url='/administracion/documentos/')),
 url(r'^documentos/$', views.documentos, name='principal' ),
 url(r'^documentos/edit/(?P<id_documento>\d+)/$', views.editardocs, name='editar_documentos'),
 url(r'^deletedocs/', views.deletedocs, name='eliminar' ),
]