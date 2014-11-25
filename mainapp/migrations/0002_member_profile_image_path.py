# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member_profile',
            name='image_path',
            field=models.CharField(default=b'gray_circle.jpg', max_length=100, null=True),
            preserve_default=True,
        ),
    ]
