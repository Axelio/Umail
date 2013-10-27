# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SubModulo.alineacion'
        db.add_column(u'submodulo', 'alineacion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Adding field 'Modulo.alineacion'
        db.add_column(u'modulo', 'alineacion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SubModulo.alineacion'
        db.delete_column(u'submodulo', 'alineacion')

        # Deleting field 'Modulo.alineacion'
        db.delete_column(u'modulo', 'alineacion')


    models = {
        u'manual_usuario.modulo': {
            'Meta': {'object_name': 'Modulo', 'db_table': "u'modulo'"},
            'alineacion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'manual_usuario.submodulo': {
            'Meta': {'object_name': 'SubModulo', 'db_table': "u'submodulo'"},
            'alineacion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modulo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manual_usuario.Modulo']"}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['manual_usuario']