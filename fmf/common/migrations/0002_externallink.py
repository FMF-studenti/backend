# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
