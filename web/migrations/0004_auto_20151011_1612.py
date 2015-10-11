# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_template_ticketexpire'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='extension',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='filename',
            field=models.FileField(upload_to=web.models.generate_download_ticket),
        ),
    ]
