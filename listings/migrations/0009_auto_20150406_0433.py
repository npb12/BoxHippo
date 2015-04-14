# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20150405_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'static/products/', verbose_name=b'Product Picture')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(verbose_name=b'Category', blank=True, to='listings.Category', null=True),
            preserve_default=True,
        ),
    ]
