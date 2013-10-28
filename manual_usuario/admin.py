# -*- coding: utf-8 -*-
from django.contrib import admin
from manual_usuario.models import Modulo, SubModulo
from manual_usuario.forms import *

class SubModuloAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    form = SubModuloForm
admin.site.register(SubModulo, SubModuloAdmin)

class ModuloAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    form = ModuloForm
admin.site.register(Modulo, ModuloAdmin)
