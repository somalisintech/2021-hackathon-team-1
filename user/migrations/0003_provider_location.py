# Generated by Django 3.2.8 on 2021-10-30 22:49

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_serviceuser_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
