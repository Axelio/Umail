# -*- coding: utf8 -*-
from django import forms
from personas.models import Personas

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Personas
        exclude = ('tipodoc','num_identificacion','email','cargo_principal','cargos_autorizados')

class FiltroForm(forms.Form):
    filtro = forms.CharField()
