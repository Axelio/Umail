# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class AuthenticacionForm(AuthenticationForm):
    username = forms.CharField(label="Correo", max_length=200)

    def __init__(self, request=None, *args, **kwargs):       
        super(AuthenticacionForm, self).__init__(*args, **kwargs)
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(u"Introduzca el usuario y/o contraseña correcta.")
            elif not self.user_cache.is_active:
                raise forms.ValidationError(u"Esta cuenta está inactiva.")
