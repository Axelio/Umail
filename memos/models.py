# -*- coding: utf8 -*-
from django.db import models
from personas.models import Personas
from django.core.exceptions import ValidationError

# Modelo para la aplicación de memos

'''
class Memos(models.Model):
    remitente               = models.ForeignKey(Personas)
    destinatario            = models.ManyToManyField('Destinatarios', blank=True, null=True)
    asunto                  = models.CharField(max_length=100)
    archivos                = models.FileField(upload_to='media/adjuntos/',null=True, blank=True)
    mensaje                 = models.TextField(max_length=2000)
    estado                  = models.ForeignKey('ClasificacionMemo')
    clasificacion           = models.CharField(blank=True, max_length=10, verbose_name=u'clasificación')
    leido                   = models.BooleanField(verbose_name=u'leído')
    class Meta:
        db_table            = u'memos'
        verbose_name_plural = u'memos'
        verbose_name        = u'memo'
    def __unicode__(self):
        return u'%s' %(self.asunto)
    def clean(self):
        if self.destinatario == None:
            raise ValidationError(u"Debe agregar algún destinatario. Por favor, corrija este error.")

class Destinatarios(models.Model):
    grupos                  = models.ForeignKey('Grupos', unique=True, null=True, blank=True)
    personas                = models.ForeignKey(Personas, unique=True, null=True, blank=True)
    class Meta:
        db_table            = u'destinatarios'
        verbose_name_plural = u'destinatarios'
        verbose_name        = u'destinatario'
    def __unicode__(self):
        if self.personas == None:
            return u'%s'%(self.grupos)
        elif self.grupos == None:
            return u'%s'%(self.personas)

class ClasificacionMemo(models.Model):
    nombre                  = models.CharField(max_length=50, unique=True)
    asignacion              = models.IntegerField(choices=((0,'Destinatario'),(1,'Remitente'),(2,'Ambos'),(3,'Nadie')), max_length=2, verbose_name = u'asignación')
    descripcion             = models.TextField(verbose_name = u'descripción', blank=True)
    class Meta:
        db_table            = u'clasificacion_memo'
        verbose_name_plural = u'clasificación de memos'
        verbose_name        = u'clasificación de memo'
    def __unicode__(self):
        return u'%s'%(self.nombre)

class Grupos(models.Model):
    nombre                  = models.CharField(max_length=50, help_text=u'Nombre del grupo')
    integrante              = models.ManyToManyField(Personas, related_name='integrante')
    jefe                    = models.ForeignKey(Personas, related_name='jefe')
    class Meta:
        db_table            = u'grupos'
        verbose_name_plural = u'grupos'
        verbose_name        = u'grupo'
    def __unicode__(self):
        return u'%s'%(self.nombre)

    def save(self, force_insert=False, force_update=False, using=None):
        if force_insert and force_update:
            raise ValueError("Cannot force both insert and updating in model saving.")
        self.save_base(using=using, force_insert=force_insert, force_update=force_update)

        from memos.models import Destinatarios
        destinatario = Destinatarios.objects.create(grupos=self)

    save.alters_data = True
'''
