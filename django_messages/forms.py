# -*- coding: utf8 -*-
import datetime
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_noop
from django.contrib.auth.models import User
from django_messages.models import *

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
else:
    notification = None

from django_messages.models import Message
from django_messages.fields import CommaSeparatedUserField

class BandejaForm(forms.Form):
    mensajes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    class Meta:
        widgets = {
              'mensaje': forms.Textarea(attrs={'rows':15, 'cols':'80%'}),
              }

from django_select2 import *
class ComposeForm(forms.ModelForm):
    recipient = ModelSelect2MultipleField(queryset=Destinatarios.objects, required=True, label='Destinatario')
    recipient.widget.set_placeholder('Usuario o grupo') # Asignar un placeholder al campo

    con_copia = ModelSelect2MultipleField(queryset=Destinatarios.objects, required=False)
    con_copia.widget.set_placeholder('Usuario o grupo') # Asignar un placeholder al campo

    class Meta:
        model = Message
        exclude = ('recipient', 'con_copia')
        fields = ('archivo', 'body', 'subject')
        widgets = {
                  'body': forms.Textarea(attrs={'rows':15, 'cols':'80%'}),
                  'subject': forms.TextInput(attrs={'placeholder':'Resumen del memorándum'}),
                  }

