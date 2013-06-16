# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
urlpatterns=patterns('',
    (r'^cambiar_clave*$', 'personas.views.password_change'), #Cambiar contraseña
    (r'^.*$', 'personas.views.perfil'), #Vista por defecto
)
