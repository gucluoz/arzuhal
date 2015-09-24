# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20150923_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='keywords',
            field=models.ManyToManyField(to='web.Keyword'),
        ),
    ]
