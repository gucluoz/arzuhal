# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='ascii_filename',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
