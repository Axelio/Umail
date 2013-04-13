# -*- coding: utf-8 -*-
from django.db import models

# Modelo para la aplicación de sedes
class Dependencias(models.Model):
    ubicacion               = models.ForeignKey('Parroquias', help_text=u'Escriba y seleccione una parroquia', verbose_name=u'ubicación')
    tipo_sede               = models.ForeignKey('TipoSede')
    departamento            = models.CharField(max_length=50)
    telefono                = models.IntegerField(unique=True, blank=True, help_text='Por favor, incluya el código de telefonía o área.', verbose_name=u'teléfono')
    nivel                   = models.ForeignKey('Niveles')
    class Meta:
        db_table            = u'dependencias'
        verbose_name_plural = u'dependencias'
        verbose_name      = u'dependencia'
    def __unicode__(self):
        return u'%s' %(self.tipo_sede)

class TipoSede(models.Model):
    nombre                  = models.CharField(max_length=20)
    class Meta:
        db_table            = u'tipo_sede'
        verbose_name_plural = u'tipo de sedes'
        verbose_name      = u'tipo de sede'
    def __unicode__(self):
        return u'%s' %(self.nombre)

class Niveles(models.Model):
    numero                  = models.IntegerField(verbose_name = u'número')
    class Meta:
        db_table            = u'niveles'
        verbose_name_plural = u'niveles'
        verbose_name        = u'nivel'
    def __unicode__(self):
        return u'%s' %(self.numero)

class Parroquias(models.Model):
    nombre                  = models.CharField(max_length=100,)
    municipio               = models.ForeignKey('Municipio')
    class Meta:
        db_table            = u'parroquia'
        verbose_name_plural = u'parroquias'
        verbose_name        = u'parroquia'
    def __unicode__(self):
        return self.nombre

class Municipio(models.Model):
    nombre                  = models.CharField(max_length=100)
    estado                  = models.ForeignKey('Estado')
    class Meta:
        db_table            = u'municipio'
        verbose_name_plural = u'municipios'
        verbose_name        = u'municipio'
    def __unicode__(self):
        return self.nombre

class Estado(models.Model):
    nombre                  = models.CharField(max_length=100)
    pais                    = models.ForeignKey('Pais',verbose_name=u'país')
    class Meta:
        db_table            = u'estado'
        verbose_name_plural = 'estados'
    def __unicode__(self):
        return u'%s'%(self.nombre)

class Pais(models.Model):
    nombre                  = models.CharField(max_length=50)
    class Meta:
    	db_table            = u'pais'
        #verbose_name_plural = 'paises'
        verbose_name_plural = u'países'
        verbose_name        = u'país'
    def __unicode__(self):
    	return "%s" % (self.nombre)


