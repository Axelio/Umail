from django.contrib import admin
from reportes.models import *
from reportes.forms import RespuestaForm

class ComentariosAdmin(admin.ModelAdmin):
    search_fields   = ['correo', 'pregunta']
    list_display    = ['correo','pregunta']
admin.site.register(Comentarios, ComentariosAdmin)

class RespuestasAdmin(admin.ModelAdmin):
    form = RespuestaForm
admin.site.register(Respuestas, RespuestasAdmin)
