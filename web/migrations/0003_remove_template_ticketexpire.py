# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_petition_ascii_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='ticketexpire',
        ),
    ]
