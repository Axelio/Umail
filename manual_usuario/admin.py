# -*- coding: utf-8 -*-
from django.contrib import admin
from manual_usuario.models import Modulo, SubModulo

class SubModuloAdmin(admin.ModelAdmin):
    list_display = ['titulo']
admin.site.register(SubModulo, SubModuloAdmin)

class ModuloAdmin(admin.ModelAdmin):
    list_display = ['titulo']
admin.site.register(Modulo, ModuloAdmin)
