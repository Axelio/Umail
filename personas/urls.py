# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from personas.views import Preguntas_Secretas, Perfil
from django.contrib.auth.forms import PasswordChangeForm

urlpatterns=patterns('',
    url(r'^preguntas_secretas/(?P<user_id>[\d]+)/$', Preguntas_Secretas.as_view(), name='preguntas_secretas'),
    url(r'^(?P<palabra_clave>\w+)_clave.*$', 'personas.views.password_change', name='cambiar_clave'),
    url(r'^.*$',Perfil.as_view(), name='perfil'),
)
