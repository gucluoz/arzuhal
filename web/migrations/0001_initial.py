# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('publishdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Date first published')),
                ('description', models.CharField(max_length=1000)),
                ('keywords', models.ManyToManyField(to='web.Keyword')),
                ('publishedby', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('containerdirectory', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=1)),
                ('filename', models.CharField(max_length=100)),
                ('downloadticket', models.CharField(max_length=32, null=True, blank=True)),
                ('ticketexpire', models.DateTimeField(null=True, verbose_name=b'Ticket expiration timestamp', blank=True)),
                ('publishdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Date first published')),
                ('petition', models.ForeignKey(to='web.Petition')),
                ('publishedby', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='petition',
            name='subject',
            field=models.ForeignKey(to='web.Subject'),
        ),
    ]
