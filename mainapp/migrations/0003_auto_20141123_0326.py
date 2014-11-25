# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_member_profile_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='member_profile',
            name='is_superuser',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sign_up_code',
            name='is_superuser',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
