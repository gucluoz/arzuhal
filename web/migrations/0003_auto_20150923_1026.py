# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_petitionkeyword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petitionkeyword',
            name='keyword',
        ),
        migrations.RemoveField(
            model_name='petitionkeyword',
            name='petition',
        ),
        migrations.DeleteModel(
            name='PetitionKeyword',
        ),
    ]
