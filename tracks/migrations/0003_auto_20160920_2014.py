# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_auto_20160920_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='track',
            name='genre',
        ),
        migrations.AddField(
            model_name='track',
            name='artists',
            field=models.ManyToManyField(to='tracks.Artist', blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='genres',
            field=models.ManyToManyField(to='tracks.Genre', blank=True),
        ),
    ]
