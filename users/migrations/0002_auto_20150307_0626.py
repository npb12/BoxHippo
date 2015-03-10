# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hideEmail',
            field=models.BooleanField(default=True, verbose_name=b'Hide Email?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='maxListings',
            field=models.IntegerField(default=1, verbose_name=b'Maximum Listings'),
            preserve_default=True,
        ),
    ]
