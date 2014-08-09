# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Team.stadium_pic'
        db.add_column('testapp1_team', 'stadium_pic',
                      self.gf('django.db.models.fields.URLField')(max_length=200, unique=True, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Team.stadium_pic'
        db.delete_column('testapp1_team', 'stadium_pic')


    models = {
        'testapp1.player': {
            'Meta': {'object_name': 'Player'},
            'alldef_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'allnba_years': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'ast': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'blk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'current_team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['testapp1.Team']", 'to_field': "'name'", 'default': "'none'", 'related_name': "'current_team'"}),
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
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'default': "''"}),
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
            'map_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'map_lat': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'map_lng': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'mvps': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'stadium': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'stadium_pic': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True', 'default': "''"}),
            'twitter': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"})
        },
        'testapp1.year': {
            'Meta': {'object_name': 'Year'},
            'all_def': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"}),
            'all_nba': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"}),
            'champion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['testapp1.Team']", 'to_field': "'name'", 'default': "'none'", 'related_name': "'champion'"}),
            'finals_logo': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'finals_mvp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['testapp1.Player']", 'to_field': "'name'", 'default': "'none'", 'related_name': "'finals_mvp'"}),
            'finals_recap': ('django.db.models.fields.TextField', [], {}),
            'highlights': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reg_mvp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['testapp1.Player']", 'to_field': "'name'", 'default': "'none'", 'related_name': "'reg_mvp'"}),
            'year': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'})
        }
    }

    complete_apps = ['testapp1']