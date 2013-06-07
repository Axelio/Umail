from personas.models import *
from django.contrib import admin
from lib import admin as Autocompletar
from django.contrib import admin
from personas.models import *

class PersonasAdmin(admin.ModelAdmin):
    search_fields   = ['num_identificacion','primer_nombre','primer_apellido','email','telefono', 'cargo_principal','cargos_autorizados']
    list_display    = ['num_identificacion','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','genero','email','telefono']
    filter_vertical = ['cargos_autorizados']
admin.site.register(Personas, PersonasAdmin)

class PersonalAdmin(admin.ModelAdmin):
    list_filter     = ['dependencia','tipo_personal']
    search_fields   = ['cargo']
admin.site.register(Personal, PersonalAdmin)

admin.site.register(TipoPersonal)
