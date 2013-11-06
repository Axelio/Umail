# -*- coding: utf8 -*-
from django import forms
from manual_usuario.models import *
from django_summernote.widgets import SummernoteWidget

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        widgets = {
              'resumen': SummernoteWidget(),
              }

class SubModuloForm(forms.ModelForm):
    class Meta:
        model = SubModulo
        widgets = {
              'resumen': SummernoteWidget(),
              }
