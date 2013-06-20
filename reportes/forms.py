# -*- coding: utf8 -*-
from django import forms
from django_messages.models import Message
from umail import settings
from django.contrib.admin import widgets
from django.forms import DateInput, TextInput

class LibroMemoForm(forms.Form):
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    class Meta:

        widgets = {
	    'fecha_inicio': DateInput(attrs={'type':'date', 'class':'w8em format-d-m-y', 'autofocus':'autofocus', 'required':'required', 'value':'','name':'fecha_inicio', 'placeholder':'fecha de inicio'}),
	    'fecha_fin': DateInput(attrs={'type':'date', 'class':'w8em format-d-m-y', 'autofocus':'autofocus', 'required':'required', 'value':'','name':'fecha_fin', 'placeholder':'fecha fin'}),
        }

    def __init__(self, *args, **kwargs):
        super(LibroMemoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].widget = self.Meta.widgets['fecha_inicio']
        self.fields['fecha_fin'].widget = self.Meta.widgets['fecha_fin']
