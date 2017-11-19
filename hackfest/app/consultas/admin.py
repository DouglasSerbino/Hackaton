# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.consultas.models import Proyecto, Consulta

# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Consulta)