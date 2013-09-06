# -*- coding: utf8 -*-
from django import forms
from personas.models import Personas
from auth.models import PreguntasSecretas
import random

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Personas
        exclude = ('tipodoc','num_identificacion','email','cargo_principal','cargos_autorizados')

class FiltroForm(forms.Form):
    filtro = forms.CharField()

class PreguntasForm(forms.Form):
    respuesta_1 = forms.CharField(widget=forms.TextInput(attrs={'required':'required'}))
    respuesta_2 = forms.CharField(widget=forms.TextInput(attrs={'required':'required'}))
    respuesta_3 = forms.CharField(widget=forms.TextInput(attrs={'required':'required'}))
