# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Meeting'
        db.create_table('drivetimes_meeting', (
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('geojsonResult', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('drivetimes', ['Meeting'])

        # Adding model 'UserCoordinate'
        db.create_table('drivetimes_usercoordinate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meeting', self.gf('django.db.models.fields.related.ForeignKey')(related_name='userCoordinates', to=orm['drivetimes.Meeting'])),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')(geography=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('transportationType', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('drivetimes', ['UserCoordinate'])

        # Adding model 'LocationType'
        db.create_table('drivetimes_locationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('drivetimes', ['LocationType'])

        # Adding model 'LocationPoint'
        db.create_table('drivetimes_locationpoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')(geography=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='locationPoints', to=orm['drivetimes.LocationType'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('drivetimes', ['LocationPoint'])


    def backwards(self, orm):
        # Deleting model 'Meeting'
        db.delete_table('drivetimes_meeting')

        # Deleting model 'UserCoordinate'
        db.delete_table('drivetimes_usercoordinate')

        # Deleting model 'LocationType'
        db.delete_table('drivetimes_locationtype')

        # Deleting model 'LocationPoint'
        db.delete_table('drivetimes_locationpoint')


    models = {
        'drivetimes.locationpoint': {
            'Meta': {'object_name': 'LocationPoint'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locationPoints'", 'to': "orm['drivetimes.LocationType']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'geography': 'True'})
        },
        'drivetimes.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'drivetimes.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'geojsonResult': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12', 'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'drivetimes.usercoordinate': {
            'Meta': {'object_name': 'UserCoordinate'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userCoordinates'", 'to': "orm['drivetimes.Meeting']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'geography': 'True'}),
            'transportationType': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['drivetimes']