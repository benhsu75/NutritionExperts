# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_expert_profile_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
