# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20151020_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
