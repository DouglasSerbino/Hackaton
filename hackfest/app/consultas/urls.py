"""hackfest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from app.consultas.views import test,ProyectosRecientes,CargarProyecto,VotacionProyecto,ComentarProyecto,ListarComentarios

urlpatterns = [
# esta url es para hacer pruebas durante el desarrollo, no tiene niguna funcionalidad especifica
    url(r'^test/', test, name='test'),
    url(r'^Proyectos/', ProyectosRecientes, name='newProjects'),
    url(r'^Proyecto/', CargarProyecto, name='cargarProyecto'),
    url(r'^ProyectoVotar/', VotacionProyecto, name='votacionProyecto'),
    url(r'^ProyectoComentar/', ComentarProyecto, name='comentarProyecto'),
    url(r'^ComentarioListar/', ListarComentarios, name='listarComentarios'),
]
