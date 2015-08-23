# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('author', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('ip', models.GenericIPAddressField(protocol='IPv4')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
