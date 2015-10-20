# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_subject_containerdirectory'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='accessCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='petition',
            name='downloadCount',
            field=models.IntegerField(default=0),
        ),
    ]
