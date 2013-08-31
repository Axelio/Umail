from django.contrib import admin
from reportes.models import *

class ComentariosAdmin(admin.ModelAdmin):
    search_fields   = ['correo', 'pregunta']
    list_display    = ['correo','pregunta']
admin.site.register(Comentarios, ComentariosAdmin)
