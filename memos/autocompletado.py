# -*- coding: utf8
'''
from memos.models import Destinatarios
from django.db.models import Q

class DestinatariosLookup(Destinatarios):
    def get_query(self,q,request):
        return Destinatarios.objects.filter(Q(personas__num_identificacion__icontains=q) | Q(personas__primer_nombre__icontains=q) | Q(personas__primer_apellido__icontains=q) | Q(grupos__nombre__icontains=q))

    def format_result(self,destinatarios):
        if not destinatarios.personas == None:
            return u'%s' % (destinatarios.personas)
        elif not destinatarios.grupos == None:
            return u'%s' % (destinatarios.grupos.nombre)

    def format_item(self,Destinatarios):
        return unicode(Destinatarios)

    def get_objects(self,ids):
        return Destinatarios.objects.filter(pk__in=ids).order_by('personas__num_identificacion','personas__primer_nombre','personas__primer_apellido','grupos__nombre')
'''
