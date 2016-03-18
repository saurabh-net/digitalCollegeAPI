# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywrapper', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_administrator',
            field=models.BooleanField(default=False),
        ),
    ]
