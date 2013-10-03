# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.borrador'
        db.add_column(u'django_messages_message', 'borrador',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Message.borrador'
        db.delete_column(u'django_messages_message', 'borrador')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        u'auth.userprofile': {
            'Meta': {'unique_together': "(('user', 'persona'),)", 'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notificaciones': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'persona': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['personas.Personas']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'django_messages.adjunto': {
            'Meta': {'object_name': 'Adjunto', 'db_table': "'adjuntos'"},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_messages.Message']"})
        },
        u'django_messages.destinatarios': {
            'Meta': {'ordering': "['usuarios__persona__primer_nombre', 'usuarios__persona__primer_apellido', 'grupos__name']", 'object_name': 'Destinatarios', 'db_table': "u'destinatarios'"},
            'grupos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuarios': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.UserProfile']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'django_messages.estadomemo': {
            'Meta': {'object_name': 'EstadoMemo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificable': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'django_messages.message': {
            'Meta': {'ordering': "['-sent_at']", 'object_name': 'Message'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'borrador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'con_copia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_ident': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent_msg': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'next_messages'", 'null': 'True', 'to': u"orm['django_messages.Message']"}),
            'read_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'received_messages'", 'to': u"orm['django_messages.Destinatarios']"}),
            'replied_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_messages'", 'to': u"orm['django_messages.Destinatarios']"}),
            'sent_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_messages.EstadoMemo']", 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'personas.personal': {
            'Meta': {'object_name': 'Personal', 'db_table': "u'personal'"},
            'cargo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cargo_principal'", 'to': u"orm['auth.Group']"}),
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sedes.Dependencias']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_personal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['personas.TipoPersonal']"})
        },
        u'personas.personas': {
            'Meta': {'object_name': 'Personas', 'db_table': "u'personas'"},
            'cargo_principal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cargo_principal'", 'to': u"orm['personas.Personal']"}),
            'cargos_autorizados': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'cargos_autorizados'", 'default': 'None', 'to': u"orm['personas.Personal']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_identificacion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'primer_apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'segundo_apellido': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'segundo_nombre': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'tipodoc': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '1'})
        },
        u'personas.tipopersonal': {
            'Meta': {'object_name': 'TipoPersonal', 'db_table': "u'tipo_personal'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'sedes.dependencias': {
            'Meta': {'object_name': 'Dependencias', 'db_table': "u'dependencias'"},
            'cargo_max': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dependencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sedes.Dependencias']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sedes.Niveles']"}),
            'siglas': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'tipo_sede': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sedes.TipoSede']"}),
            'ubicacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sedes.Parroquias']"})
        },
        u'sedes.estado': {
            'Meta': {'object_name': 'Estado', 'db_table': "u'estado'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sedes.Pais']"})
        },
        u'sedes.municipio': {
            'Meta': {'object_name': 'Municipio', 'db_table': "u'municipio'"},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sedes.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sedes.niveles': {
            'Meta': {'object_name': 'Niveles', 'db_table': "u'niveles'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'sedes.pais': {
            'Meta': {'object_name': 'Pais', 'db_table': "u'pais'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'sedes.parroquias': {
            'Meta': {'object_name': 'Parroquias', 'db_table': "u'parroquia'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sedes.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sedes.tiposede': {
            'Meta': {'object_name': 'TipoSede', 'db_table': "u'tipo_sede'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['django_messages']