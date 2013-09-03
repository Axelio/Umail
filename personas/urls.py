# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from personas.views import PreguntasSecretas, Cambiar_Clave
from auth.forms import PreguntasForm
from django.contrib.auth.forms import PasswordChangeForm

urlpatterns=patterns('',
    url(r'^cambiar_clave$', PreguntasSecretas.as_view(), name='cambiar_clave'), #Cambiar contraseña

    (r'^.*$', 'personas.views.perfil'), #Vista por defecto

)
