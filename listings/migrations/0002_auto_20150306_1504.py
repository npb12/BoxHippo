# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Listing Description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='webpage',
            field=models.CharField(max_length=144, null=True, verbose_name=b'Listing Webpage', blank=True),
            preserve_default=True,
        ),
    ]
