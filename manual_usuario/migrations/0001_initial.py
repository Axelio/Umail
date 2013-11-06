# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Modulo'
        db.create_table(u'modulo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('resumen', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'manual_usuario', ['Modulo'])

        # Adding model 'SubModulo'
        db.create_table(u'submodulo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modulo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['manual_usuario.Modulo'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('resumen', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'manual_usuario', ['SubModulo'])


    def backwards(self, orm):
        # Deleting model 'Modulo'
        db.delete_table(u'modulo')

        # Deleting model 'SubModulo'
        db.delete_table(u'submodulo')


    models = {
        u'manual_usuario.modulo': {
            'Meta': {'object_name': 'Modulo', 'db_table': "u'modulo'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'manual_usuario.submodulo': {
            'Meta': {'object_name': 'SubModulo', 'db_table': "u'submodulo'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modulo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manual_usuario.Modulo']"}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['manual_usuario']