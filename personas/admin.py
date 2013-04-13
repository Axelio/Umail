from personas.models import *
from django.contrib import admin
from lib import admin as Autocompletar
from django.contrib import admin
from personas.models import *

class PersonasAdmin(admin.ModelAdmin):
    search_fields   =['num_identificacion','primer_nombre','primer_apellido','email','telefono']
    list_display    = ['num_identificacion','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','genero','email','telefono']
    search_fields   = ['cargo_principal','cargos_autorizados']
admin.site.register(Personas, PersonasAdmin)

class CargosAdmin(admin.ModelAdmin):
    list_display    = ['nombre']
    search_fields   = ['nombre']
admin.site.register(Cargos, CargosAdmin)

class PermisosAdmin(admin.ModelAdmin):
    list_display    = ['nombre']
    search_fields   = ['nombre']
admin.site.register(Permisos, PermisosAdmin)
