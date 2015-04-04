# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20150307_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='freqType',
            field=models.CharField(default=b'M', max_length=2, verbose_name=b'Frequency Type', choices=[(b'D', b'Daily'), (b'W', b'Weekly'), (b'M', b'Monthly'), (b'Q', b'Quarterly'), (b'S', b'Semi-Annually'), (b'A', b'Annually')]),
            preserve_default=True,
        ),
    ]
