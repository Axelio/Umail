# -*- coding: utf8 -*-
from django.db import models
from sedes.models import Niveles, Dependencias
from django.dispatch import receiver
from django.db.models.signals import post_save

ALINEADO = (('Derecha','Derecha'),('Izquierda','Izquierda'))
class Modulo(models.Model):
    titulo = models.CharField(max_length=100, verbose_name=u'título',)
    alineacion = models.CharField(max_length=10,choices=ALINEADO, default='', verbose_name=u'alineación')
    imagen = models.ImageField(upload_to='manual/',null=True, blank=True)
    resumen = models.TextField()
    class Meta:
        db_table            = u'modulo'
        verbose_name        = u'módulo'
    def __unicode__(self):
        return u'%s' %(self.titulo)

class SubModulo(models.Model):
    modulo = models.ForeignKey('Modulo', verbose_name=u'módulo')
    titulo = models.CharField(max_length=100, verbose_name=u'título')
    alineacion = models.CharField(max_length=10,choices=ALINEADO, default='', verbose_name=u'alineación')
    imagen = models.ImageField(upload_to='manual/',null=True, blank=True)
    resumen = models.TextField()
    class Meta:
        db_table            = u'submodulo'
        verbose_name        = u'submódulo'
    def __unicode__(self):
        return u'%s' %(self.titulo)
