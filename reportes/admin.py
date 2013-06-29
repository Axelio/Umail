from django.contrib import admin
from reportes.models import *

class ComentariosAdmin(admin.ModelAdmin):
    search_fields   = ['correo']
    list_display    = ['correo','sentimiento','pregunta']
admin.site.register(Comentarios, ComentariosAdmin)
