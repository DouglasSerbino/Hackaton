# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import User, Recompensa

class UserAdmin(admin.ModelAdmin):
	list_display=('username','nivel','puntuacion','recompensa','last_name','email',)


admin.site.register(User,UserAdmin)
admin.site.register(Recompensa)