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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('coach', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('gm', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=200, unique=True)),
            ('twitter_widget', self.gf('django.db.models.fields.CharField')(max_length=500, default='')),
            ('logo', self.gf('django.db.models.fields.URLField')(max_length=200, unique=True)),
        ))
        db.send_create_signal('testapp1', ['Team'])

        # Adding model 'Player'
        db.create_table('testapp1_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('years_exp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=200, unique=True)),
            ('twitter_widget', self.gf('django.db.models.fields.CharField')(max_length=500, default='')),
            ('photo', self.gf('django.db.models.fields.URLField')(max_length=200, unique=True)),
            ('highlights', self.gf('django.db.models.fields.URLField')(max_length=200, default='', unique=True)),
        ))
        db.send_create_signal('testapp1', ['Player'])

        # Adding model 'Year'
        db.create_table('testapp1_year', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, unique=True)),
            ('finals_logo', self.gf('django.db.models.fields.URLField')(max_length=200, unique=True)),
            ('finals_recap', self.gf('django.db.models.fields.TextField')()),
            ('highlights', self.gf('django.db.models.fields.URLField')(max_length=200, default='', unique=True)),
        ))
        db.send_create_signal('testapp1', ['Year'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table('testapp1_team')

        # Deleting model 'Player'
        db.delete_table('testapp1_player')

        # Deleting model 'Year'
        db.delete_table('testapp1_year')


    models = {
        'testapp1.player': {
            'Meta': {'object_name': 'Player'},
            'education': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'highlights': ('django.db.models.fields.URLField', [], {'max_length': '200', 'default': "''", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'gm': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"})
        },
        'testapp1.year': {
            'Meta': {'object_name': 'Year'},
            'finals_logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'}),
            'finals_recap': ('django.db.models.fields.TextField', [], {}),
            'highlights': ('django.db.models.fields.URLField', [], {'max_length': '200', 'default': "''", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'unique': 'True'})
        }
    }

    complete_apps = ['testapp1']