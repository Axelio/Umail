from django.contrib import admin
from reportes.models import *
from reportes.forms import RespuestaForm, ComentariosForm

class RespuestasInline(admin.TabularInline):
    model           = Respuestas
    form            = RespuestaForm
    max_num         = 1

class ComentariosAdmin(admin.ModelAdmin):
    search_fields   = ['correo', 'pregunta']
    list_display    = ['correo','pregunta']
    inlines         = (RespuestasInline,)
    form            = ComentariosForm
admin.site.register(Comentarios, ComentariosAdmin)

class RespuestasAdmin(admin.ModelAdmin):
    form            = RespuestaForm
admin.site.register(Respuestas, RespuestasAdmin)
