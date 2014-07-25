# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table('testapp1_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('location', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('coach', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('gm', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('twitter', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
            ('twitter_widget', self.gf('django.db.models.fields.CharField')(default='', max_length=500)),
            ('logo', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
            ('finals_years', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('mvps', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('finals_mvps', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal('testapp1', ['Team'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table('testapp1_team')


    models = {
        'testapp1.player': {
            'Meta': {'object_name': 'Player'},
            'education': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'highlights': ('django.db.models.fields.URLField', [], {'unique': 'True', 'default': "''", 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'photo': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'twitter': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'years_exp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'testapp1.team': {
            'Meta': {'object_name': 'Team'},
            'coach': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'finals_mvps': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'finals_years': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'gm': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'logo': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'mvps': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'twitter': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'})
        },
        'testapp1.year': {
            'Meta': {'object_name': 'Year'},
            'finals_logo': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'finals_recap': ('django.db.models.fields.TextField', [], {}),
            'highlights': ('django.db.models.fields.URLField', [], {'unique': 'True', 'default': "''", 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'})
        }
    }

    complete_apps = ['testapp1']