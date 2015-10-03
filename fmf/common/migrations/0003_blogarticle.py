# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_externallink'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=256)),
                ('published', models.DateTimeField()),
            ],
            options={
                'managed': False,
            },
        ),
    ]
