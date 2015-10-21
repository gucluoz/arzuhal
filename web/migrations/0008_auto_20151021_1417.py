# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_petition_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petition',
            name='accessCount',
            field=models.IntegerField(default=0, verbose_name=b'G\xc3\xb6r\xc3\xbcnt\xc3\xbcleme'),
        ),
        migrations.AlterField(
            model_name='petition',
            name='description',
            field=models.TextField(verbose_name=b'A\xc3\xa7\xc4\xb1klama'),
        ),
        migrations.AlterField(
            model_name='petition',
            name='downloadCount',
            field=models.IntegerField(default=0, verbose_name=b'\xc4\xb0ndirme'),
        ),
        migrations.AlterField(
            model_name='petition',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name=b'Aktif?'),
        ),
        migrations.AlterField(
            model_name='petition',
            name='keywords',
            field=models.ManyToManyField(to='web.Keyword', verbose_name=b'Anahtar Kelimeler', blank=True),
        ),
        migrations.AlterField(
            model_name='petition',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'\xc4\xb0sim'),
        ),
        migrations.AlterField(
            model_name='petition',
            name='subject',
            field=models.ForeignKey(verbose_name=b'Konu', to='web.Subject'),
        ),
    ]
