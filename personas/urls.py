# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from personas.views import Cambiar_Clave
from auth.forms import PreguntasForm
from django.contrib.auth.forms import PasswordChangeForm

urlpatterns=patterns('',
    url(r'^cambiar_clave$', Cambiar_Clave.as_view([PreguntasForm, PasswordChangeForm]), name='cambiar_clave'), #Cambiar contraseña

    (r'^.*$', 'personas.views.perfil'), #Vista por defecto

)
