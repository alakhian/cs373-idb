# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Player.fgperc'
        db.add_column('testapp1_player', 'fgperc',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Player.ftperc'
        db.add_column('testapp1_player', 'ftperc',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Player.reb'
        db.add_column('testapp1_player', 'reb',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Player.ast'
        db.add_column('testapp1_player', 'ast',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Player.blk'
        db.add_column('testapp1_player', 'blk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Player.stl'
        db.add_column('testapp1_player', 'stl',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Player.pts'
        db.add_column('testapp1_player', 'pts',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Player.finals_years'
        db.add_column('testapp1_player', 'finals_years',
                      self.gf('django.db.models.fields.CharField')(max_length=200, default=''),
                      keep_default=False)

        # Adding field 'Player.finals_teams'
        db.add_column('testapp1_player', 'finals_teams',
                      self.gf('django.db.models.fields.CharField')(max_length=500, default=''),
                      keep_default=False)

        # Adding field 'Player.mvp_years'
        db.add_column('testapp1_player', 'mvp_years',
                      self.gf('django.db.models.fields.CharField')(max_length=200, default=''),
                      keep_default=False)

        # Adding field 'Player.finalsmvp_years'
        db.add_column('testapp1_player', 'finalsmvp_years',
                      self.gf('django.db.models.fields.CharField')(max_length=200, default=''),
                      keep_default=False)

        # Adding field 'Player.allnba_years'
        db.add_column('testapp1_player', 'allnba_years',
                      self.gf('django.db.models.fields.CharField')(max_length=200, default=''),
                      keep_default=False)

        # Adding field 'Player.alldef_years'
        db.add_column('testapp1_player', 'alldef_years',
                      self.gf('django.db.models.fields.CharField')(max_length=200, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Player.fgperc'
        db.delete_column('testapp1_player', 'fgperc')

        # Deleting field 'Player.ftperc'
        db.delete_column('testapp1_player', 'ftperc')

        # Deleting field 'Player.reb'
        db.delete_column('testapp1_player', 'reb')

        # Deleting field 'Player.ast'
        db.delete_column('testapp1_player', 'ast')

        # Deleting field 'Player.blk'
        db.delete_column('testapp1_player', 'blk')

        # Deleting field 'Player.stl'
        db.delete_column('testapp1_player', 'stl')

        # Deleting field 'Player.pts'
        db.delete_column('testapp1_player', 'pts')

        # Deleting field 'Player.finals_years'
        db.delete_column('testapp1_player', 'finals_years')

        # Deleting field 'Player.finals_teams'
        db.delete_column('testapp1_player', 'finals_teams')

        # Deleting field 'Player.mvp_years'
        db.delete_column('testapp1_player', 'mvp_years')

        # Deleting field 'Player.finalsmvp_years'
        db.delete_column('testapp1_player', 'finalsmvp_years')

        # Deleting field 'Player.allnba_years'
        db.delete_column('testapp1_player', 'allnba_years')

        # Deleting field 'Player.alldef_years'
        db.delete_column('testapp1_player', 'alldef_years')


    models = {
        'testapp1.player': {
            'Meta': {'object_name': 'Player'},
            'alldef_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'allnba_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'ast': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'blk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fgperc': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'finals_teams': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"}),
            'finals_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'finalsmvp_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'ftperc': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'gp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'highlights': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mvp_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'photo': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'pts': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reb': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'stl': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'twitter': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"}),
            'years_exp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'testapp1.team': {
            'Meta': {'object_name': 'Team'},
            'coach': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'finals_mvps': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'finals_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'gm': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'logo': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'mvps': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'twitter': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"})
        },
        'testapp1.year': {
            'Meta': {'object_name': 'Year'},
            'finals_logo': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'finals_recap': ('django.db.models.fields.TextField', [], {}),
            'highlights': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'})
        }
    }

    complete_apps = ['testapp1']