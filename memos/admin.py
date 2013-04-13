# -*- coding: utf8 -*-
from django.contrib import admin
from memos.models import *
#from memos.forms import MemosForm
from lib import admin as Autocompletar

'''
class MemosAdmin(admin.ModelAdmin):
    list_display    = ('remitente', 'leido', 'clasificacion', 'estado')
    search_fields   = ('remitente',)
    horizontal_filter = ('destintario',)
    form            = MemosForm
admin.site.register(Memos, MemosAdmin)

class ClasificacionMemoAdmin(admin.ModelAdmin):
    list_display    = ('nombre','asignacion')
admin.site.register(ClasificacionMemo, ClasificacionMemoAdmin)

class GruposAdmin(Autocompletar.Autocompletar):
    form            = Autocompletar.make_ajax_form(Grupos,dict(jefe='personas'))
    list_display    = ('nombre','jefe')
    search_fields   = ('nombre','jefe__primer_apellido','jefe__primer_nombre')
admin.site.register(Grupos, GruposAdmin)

class DestinatariosAdmin(admin.ModelAdmin):
    list_display    = ('id','grupos','personas')
    ordering        = ('id',)
admin.site.register(Destinatarios, DestinatariosAdmin)
'''
