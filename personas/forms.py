# -*- coding: utf8 -*-
from django import forms
from personas.models import Personas
from auth.models import PreguntasSecretas

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Personas
        exclude = ('tipodoc','num_identificacion','email','cargo_principal','cargos_autorizados')

class FiltroForm(forms.Form):
    filtro = forms.CharField()

class PreguntasForm(forms.ModelForm):
    respuesta_s = forms.CharField(label='Respuesta')
    class Meta:
        model = PreguntasSecretas
        exclude = ('respuesta','usuario')

    '''
    def __init__(self, *args, **kwargs):
        super(PreguntasForm, self).__init__(*args, **kwargs)
        self.fields['pregunta'].widget.attrs['disabled'] = True
    '''
