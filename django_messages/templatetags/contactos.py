# -*- coding: utf8 -*-
from django import template
from django.utils.html import escape

register = template.Library()
def telefono(numero):
    if numero == None:
        numero = 'Ninguno'
    return numero
telefono.is_safe = True 
register.filter(telefono)
