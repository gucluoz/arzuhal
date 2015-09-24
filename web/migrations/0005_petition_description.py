# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_petition_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='description',
            field=models.CharField(default=' ', max_length=1000),
            preserve_default=False,
        ),
    ]
