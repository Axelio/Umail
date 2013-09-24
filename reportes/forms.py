# -*- coding: utf8 -*-
from django import forms
from django_messages.models import Message
from umail import settings
from django.contrib.admin import widgets
from django.utils.safestring import mark_safe
from reportes.models import Comentarios, Respuestas
from suit_redactor.widgets import RedactorWidget
from suit_ckeditor.widgets import CKEditorWidget

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
      return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

OPCIONES = (('entrada', 'Entrada',), ('salida', 'Salida',), ('ambos','Ambos'))
class LibroMemoForm(forms.Form):
    opcion = forms.ChoiceField(choices=OPCIONES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
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
        if not self.cleaned_data['codigo'] == None:
            return self.cleaned_data


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuestas
        widgets = {
                  'comentario': RedactorWidget(editor_options={'lang': 'es'})
                  }
    ordering = ('-respondido',)

