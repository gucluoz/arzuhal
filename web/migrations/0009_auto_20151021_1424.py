# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20151021_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='extension',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Uzant\xc4\xb1', blank=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='filename',
            field=models.FileField(upload_to=web.models.generate_download_ticket, verbose_name=b'Dosya ad\xc4\xb1'),
        ),
        migrations.AlterField(
            model_name='template',
            name='publishdate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Yay\xc4\xb1n Tarihi'),
        ),
        migrations.AlterField(
            model_name='template',
            name='publishedby',
            field=models.ForeignKey(verbose_name=b'Yay\xc4\xb1nlayan', to=settings.AUTH_USER_MODEL),
        ),
    ]
