# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20150306_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.DecimalField(null=True, verbose_name=b'Price', max_digits=9, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
