# -*- coding: utf8 -*-
from django import template
from django.utils.html import escape
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

register = template.Library()
def accion(accion_id):
    log_user = LogEntry.objects.get(id=accion_id)
    if log_user.is_addition:
        return "Usted ha adicionado"
    elif log_user.is_change:
        return "Usted ha modificado"
    elif log_user.is_deletion:
        return "Usted ha eliminado"
accion.is_safe = True 
register.filter(accion)

