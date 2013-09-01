# -*- coding: utf8 -*-
from django import forms
from personas.models import Personas

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Personas
        exclude = ('tipodoc','num_identificacion','email','cargo_principal','cargos_autorizados')

class FiltroForm(forms.Form):
    filtro = forms.CharField()

class PreguntasRespuestasForm(forms.Form):
    pregunta1 = forms.CharField(label='Pregunta secreta')
    respuesta1 = forms.CharField(label='Respuesta')
    pregunta2 = forms.CharField(label='Pregunta secreta')
    respuesta2 = forms.CharField(label='Respuesta')
    pregunta3 = forms.CharField(label='Pregunta secreta')
    respuesta3 = forms.CharField(label='Respuesta')
