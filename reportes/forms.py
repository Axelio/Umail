# -*- coding: utf8 -*-
from django import forms
from django_messages.models import Message
from umail import settings
from django.contrib.admin import widgets

class LibroMemoForm(forms.Form):
    fecha_inicio = forms.CharField()
    fecha_fin = forms.CharField()
    class Meta:

        widgets = {
	    'fecha_inicio': forms.TextInput(attrs={'type':'text', 'class':'w8em format-d-m-y', 'autofocus':'autofocus', 'required':'required', 'value':'','name':'fecha_inicio','id':'datepicker1','placeholder':'fecha inicial'}),
	    'fecha_fin': forms.TextInput(attrs={'type':'text', 'class':'w8em format-d-m-y', 'required':'required', 'value':'','name':'fecha_fin','id':'datepicker2','placeholder':'fecha final'}),
        }

    def __init__(self, *args, **kwargs):
        super(LibroMemoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].widget = self.Meta.widgets['fecha_inicio']
        self.fields['fecha_fin'].widget = self.Meta.widgets['fecha_fin']
    '''
        self.fields['hora'].widget = forms.HiddenInput()
    '''
