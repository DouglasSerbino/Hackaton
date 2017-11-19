from django.conf.urls import url
from django.contrib import admin

# Importando vistas de la app gamificacion
from app.gamificacion import views

# URLs para la app Gamificacion
urlpatterns = [
    url(r'^gamificacion/index/$', views.principal, name='principal'),
]
