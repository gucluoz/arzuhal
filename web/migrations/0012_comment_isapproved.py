# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20151029_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='isApproved',
            field=models.BooleanField(default=True, verbose_name=b'Onay?'),
        ),
    ]
