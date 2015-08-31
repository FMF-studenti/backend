# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=256)),
                ('messages', models.IntegerField()),
                ('avatar', models.CharField(max_length=256)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
