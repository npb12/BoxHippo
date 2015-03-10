# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('companyName', models.CharField(max_length=144, null=True, verbose_name=b'Company Name', blank=True)),
                ('website', models.URLField(verbose_name=b'Website')),
                ('facebook', models.URLField(null=True, verbose_name=b'Facebook Page', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, verbose_name=b'Email', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['companyName'],
            },
            bases=(models.Model,),
        ),
    ]
