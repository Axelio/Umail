# -*- coding: utf8 -*-
from django import template
from django.utils.html import escape
from django.utils.html import format_html
from django_messages.models import Message
from auth.models import User

register = template.Library()
def responder_memo(memo,arg):
    memo = Message.objects.get(id=memo)
    user = User.objects.get(id=arg)

    for dest in memo.con_copia.get_query_set():
        if dest.usuarios.user.pk == user.pk:
            tabla = '<table></td><td width=100% align="left"><div class="rc_btn_02"><a href="/eliminar/' + str(memo.id) + '">Eliminar</a></div></td></tr></table>'
            con_copia=True


    for dest in memo.recipient.get_query_set():
        if dest.usuarios.user.pk == user.pk and not con_copia:
            tabla = '<table><tr><td width=50%><div class="rc_btn_02"><a href="/responder/' + str(memo.id) + '">Responder</a></div></td><td width=50% align="left"><div class="rc_btn_02"><a href="/eliminar/' + str(memo.id) + '">Eliminar</a></div></td></tr></table>'

    return format_html(tabla)
responder_memo.is_safe = True 
register.filter(responder_memo)
