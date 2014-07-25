# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Team.owner'
        db.alter_column('testapp1_team', 'owner', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'Team.owner'
        db.alter_column('testapp1_team', 'owner', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        'testapp1.player': {
            'Meta': {'object_name': 'Player'},
            'alldef_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'allnba_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'ast': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'blk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'current_team': ('django.db.models.fields.related.ForeignKey', [], {'default': "'none'", 'to_field': "'name'", 'related_name': "'current_team'", 'to': "orm['testapp1.Team']"}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fgperc': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'finals_teams': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"}),
            'finals_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'finalsmvp_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'ftperc': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'gp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'highlights': ('django.db.models.fields.URLField', [], {'max_length': '200', 'default': "''", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mvp_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'pts': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reb': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'stl': ('django.db.models.fields.FloatField', [], {'default': '0'}),
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
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"})
        },
        'testapp1.year': {
            'Meta': {'object_name': 'Year'},
            'all_def': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"}),
            'all_nba': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"}),
            'champion': ('django.db.models.fields.related.ForeignKey', [], {'default': "'none'", 'to_field': "'name'", 'related_name': "'champion'", 'to': "orm['testapp1.Team']"}),
            'finals_logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'finals_mvp': ('django.db.models.fields.related.ForeignKey', [], {'default': "'none'", 'to_field': "'name'", 'related_name': "'finals_mvp'", 'to': "orm['testapp1.Player']"}),
            'finals_recap': ('django.db.models.fields.TextField', [], {}),
            'highlights': ('django.db.models.fields.URLField', [], {'max_length': '200', 'default': "''", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'unique': 'True'})
        }
    }

    complete_apps = ['testapp1']