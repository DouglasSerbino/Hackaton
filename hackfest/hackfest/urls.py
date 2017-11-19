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
from django.conf.urls import url, include
from django.contrib import admin

from app.archivos import views 

urlpatterns = [
    #URL DE LAS AREAS PUBLICAS DE LA APLICACION
	url(r'^$', views.inicio, name="inicio"),
    url(r'^documentos/', views.documentacion, name="documentacion"),

    #NOMBRES DE ESPACIO DE URLS ABSOLUTAS DE LAS APPS
    url(r'^admin/', admin.site.urls),

    url(r'^consultas/', include('app.consultas.urls')),

    url(r'^administracion/', include('app.archivos.urls', namespace="archivos")),
    url(r'^', include('app.gamificacion.urls', namespace='gamificacion')),

    #NOMBRES DE ESPACIO PARA LAS URLS DEL RESTFULL
    url(r'^gamification/rest/', include('app.restviews.urls', namespace="restfull")),

]
