# -*- coding: utf-8 -*-
from django.template import Library, Node, TemplateSyntaxError
from django.utils.html import format_html

class InboxOutput(Node):
    def __init__(self, varname=None):
        self.varname = varname
        
    def render(self, context):
        try:
            user = context['user']
            count = user.received_messages.filter(read_at__isnull=True, recipient_deleted_at__isnull=True).count()
        except (KeyError, AttributeError):
            count = ''
        if self.varname is not None:
            context[self.varname] = count
            return ""
        else:
            return "%s" % (count)        
        
def do_print_inbox_count(parser, token):
    """
    A templatetag to show the unread-count for a logged in user.
    Returns the number of unread messages in the user's inbox.
    Usage::
    
        {% load inbox %}
        {% inbox_count %}
    
        {# or assign the value to a variable: #}
        
        {% inbox_count as my_var %}
        {{ my_var }}
        
    """
    bits = token.contents.split()
    if len(bits) > 1:
        if len(bits) != 3:
            raise TemplateSyntaxError, "inbox_count tag takes either no arguments or exactly two arguments"
        if bits[1] != 'as':
            raise TemplateSyntaxError, "first argument to inbox_count tag must be 'as'"
        return InboxOutput(bits[2])
    else:
        return InboxOutput()

register = Library()     
register.tag('inbox_count', do_print_inbox_count)


@register.filter(name="negrillas", is_safe=True)
def negrillas(request,id_message):
    from django_messages.models import Message, Destinatarios
    mensaje = Message.objects.get(id=id_message)
    destinatario = Destinatarios.objects.get(usuarios__user=request.user)
    # Si esta entre los leídos, retornar False para que NO renderice negrillas
    if destinatario in mensaje.leido_por.get_query_set():
        return False
    else:
        return True
    
register.filter(negrillas)


@register.filter(name="destin", is_safe=True)
def destin(tipo_dest,id_message):
    from django_messages.models import Message

    mensajes = ''
    if tipo_dest == 'sender':
        return Message.objects.get(id=id_message).sender
    else:
        mensaje = Message.objects.get(id=id_message)
        mensajes = Message.objects.filter(codigo=mensaje.codigo).exclude(con_copia=True)
        if mensajes.count() > 1:
            destinatario = str(mensajes[0].recipient)
            return u'%s... y %s más' %(destinatario[:23], mensajes.count()-1)
        else:
            destinatario = Message.objects.get(id=id_message).recipient
            return str(destinatario)[:23] + '...'
register.filter(destin)

@register.filter(name="icon_status", is_safe=True)
def icon_status(id_message):
    from django_messages.models import Message
    memo = Message.objects.get(id=id_message)
    if memo.status.nombre == 'Aprobado':
        icono = '<i class="icon-ok" style="color:#2BC243"></i>'
    elif memo.status.nombre == 'Anulado':
        icono = '<i class="icon-remove" style="color:#EA4444"></i>'
    elif memo.status.nombre == 'En espera':
        icono = '<i class="icon-time" style="color:#0088CC"></i>'
    return format_html(icono)
register.filter(icon_status)
