# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20151011_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='containerdirectory',
        ),
    ]
