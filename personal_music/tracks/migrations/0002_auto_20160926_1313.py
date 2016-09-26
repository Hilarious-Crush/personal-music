# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='genre',
        ),
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.ForeignKey(to='tracks.Genre', default=1),
            preserve_default=False,
        ),
    ]
