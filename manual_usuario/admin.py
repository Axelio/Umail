from manual_usuario.models import *
from django.contrib import admin

class ManualDetallesInline(admin.TabularInline):
    model = Manual_Detalles
    extra = 1

class ManualAdmin(admin.ModelAdmin):
    search_fields   = ['titulo','seccion']
    list_display    = ['titulo','seccion']
    inlines = [ManualDetallesInline]
admin.site.register(Manual, ManualAdmin)
