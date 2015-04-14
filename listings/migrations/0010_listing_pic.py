# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_auto_20150406_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='pic',
            field=models.ForeignKey(verbose_name=b'Product Picture', blank=True, to='listings.ProductPicture', null=True),
            preserve_default=True,
        ),
    ]
