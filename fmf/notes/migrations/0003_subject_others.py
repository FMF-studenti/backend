# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_level_years'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='others',
            field=models.BooleanField(default=False),
        ),
    ]
