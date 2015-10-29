# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_searchrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Ad Soyad')),
                ('email', models.CharField(max_length=200, verbose_name=b'E-Posta')),
                ('comment', models.TextField(verbose_name=b'Yorum')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='petition',
            name='ascii_filename',
            field=models.CharField(max_length=200, verbose_name=b'URL G\xc3\xb6r\xc3\xbcnen Ad [Dikkat!]', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='petition',
            field=models.ForeignKey(blank=True, to='web.Petition', null=True),
        ),
    ]
