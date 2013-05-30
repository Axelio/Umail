# -*- coding: utf8 -*-
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.text import wrap

register = template.Library()

@register.filter(name="disminuir", is_safe=True)
def disminuir(texto, arg):
    return texto.rstrip()[:arg] + '... '
register.filter(disminuir)

@register.filter(name="disminuir_t", is_safe=True)
def disminuir_t(texto, arg):
    return texto.rstrip()[:arg]
register.filter(disminuir_t)
