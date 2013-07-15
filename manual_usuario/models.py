# -*- coding: utf8 -*-
from django.db import models

OPCIONES = (
    ('Memos', 'Memos'),
    ('Reportes', 'Reportes'),
    ('Perfiles', 'Perfiles'),
    ('Contactos', 'Contactos'),
    ('Noticias', 'Noticias'),
)

class Manual_Detalles(models.Model):
    manual = models.ForeignKey('Manual')
    texto = models.TextField()
    imagen = models.ImageField(upload_to='manual_imagenes/')
    class Meta:
        db_table            = u'manual_usuario_detalles'
        verbose_name_plural = u'detalles manuales de usuario'
    def __unicode__(self):
        return u'%s'%(self.manual)
    

class Manual(models.Model):
    titulo = models.CharField(max_length=100, verbose_name=u'título')
    seccion = models.CharField(max_length=15, choices=OPCIONES, verbose_name=u'sección')
    class Meta:
        db_table            = u'manual_usuario'
        verbose_name_plural = u'manuales de usuario'
    def __unicode__(self):
        return u'%s'%(self.titulo)

