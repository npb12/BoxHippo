# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0003_auto_20150307_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(default=1, verbose_name=b'Listing Owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
