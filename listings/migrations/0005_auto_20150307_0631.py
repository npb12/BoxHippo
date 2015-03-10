# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='rating',
            field=models.DecimalField(default=0, verbose_name=b'Rating', max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='webpage',
            field=models.URLField(null=True, verbose_name=b'Listing Webpage', blank=True),
            preserve_default=True,
        ),
    ]
