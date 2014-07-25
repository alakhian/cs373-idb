# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Player.gp'
        db.add_column('testapp1_player', 'gp',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.gs'
        db.add_column('testapp1_player', 'gs',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.minpg'
        db.add_column('testapp1_player', 'minpg',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Player.gp'
        db.delete_column('testapp1_player', 'gp')

        # Deleting field 'Player.gs'
        db.delete_column('testapp1_player', 'gs')

        # Deleting field 'Player.minpg'
        db.delete_column('testapp1_player', 'minpg')


    models = {
        'testapp1.player': {
            'Meta': {'object_name': 'Player'},
            'education': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'gp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'highlights': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"}),
            'years_exp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'testapp1.team': {
            'Meta': {'object_name': 'Team'},
            'coach': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'finals_mvps': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'finals_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'gm': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'mvps': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"})
        },
        'testapp1.year': {
            'Meta': {'object_name': 'Year'},
            'finals_logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'finals_recap': ('django.db.models.fields.TextField', [], {}),
            'highlights': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'unique': 'True'})
        }
    }

    complete_apps = ['testapp1']