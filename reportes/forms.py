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
            'fecha_inicio': forms.TextInput(attrs={'type':'text', 'class':'input', 'required':'required', 'value':'','name':'fecha_inicio','id':'datepicker1','placeholder':'fecha inicial'}),
            'fecha_fin': forms.TextInput(attrs={'type':'text', 'class':'input', 'required':'required', 'value':'','name':'fecha_fin','id':'datepicker2','placeholder':'fecha final'}),
            }

    def __init__(self, *args, **kwargs):
        super(LibroMemoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].widget = self.Meta.widgets['fecha_inicio']
        self.fields['fecha_fin'].widget = self.Meta.widgets['fecha_fin']

class ConsultaMemoForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('recipient','con_copia','subject','body','sender','parent_msg','sent_at','read_at','replied_at','sender_deleted_at','recipient_deleted_at','status','tipo','leido_por','num_ident')
        widgets = {
            'codigo': forms.TextInput(attrs={'class':'input', 'required':'required', 'value':'','placeholder':'código del memo'}),
            }
    def clean_codigo(self):
        return self.cleaned_data

