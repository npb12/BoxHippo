# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_category_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(verbose_name=b'Main Category', blank=True, to='listings.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='subCategory',
            field=models.ForeignKey(verbose_name=b'Sub Category', blank=True, to='listings.SubCategory', null=True),
            preserve_default=True,
        ),
    ]
