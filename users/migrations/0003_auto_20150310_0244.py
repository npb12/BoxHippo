# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150307_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='maxListings',
            field=models.IntegerField(default=0, verbose_name=b'Maximum Listings'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(null=True, verbose_name=b'Website', blank=True),
            preserve_default=True,
        ),
    ]
