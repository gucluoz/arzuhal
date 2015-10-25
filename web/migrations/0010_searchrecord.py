# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20151021_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=200, verbose_name=b'Arama metni')),
                ('searchTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Arama tarihi')),
                ('resultcount', models.IntegerField(default=0)),
            ],
        ),
    ]
