# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='needs_to_update_password',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
