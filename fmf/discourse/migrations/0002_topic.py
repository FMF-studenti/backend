# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=256)),
                ('updated', models.DateTimeField()),
                ('last_poster', models.CharField(max_length=256)),
                ('last_poster_avatar', models.CharField(max_length=256)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
