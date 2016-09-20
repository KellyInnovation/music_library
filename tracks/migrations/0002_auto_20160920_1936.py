# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='track_number',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(to='tracks.Artist', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.ForeignKey(to='tracks.Genre', null=True, blank=True),
        ),
    ]
