# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20141125_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert_profile',
            name='is_superuser',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
