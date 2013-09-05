# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from personas.views import Preguntas_Secretas
from django.contrib.auth.forms import PasswordChangeForm

urlpatterns=patterns('',
    url(r'^preguntas_secretas$', Preguntas_Secretas.as_view(), name='preguntas_secretas'),

    (r'^.*$', 'personas.views.perfil'), #Vista por defecto

)
