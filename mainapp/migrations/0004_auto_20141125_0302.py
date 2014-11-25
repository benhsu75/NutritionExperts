# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20141123_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='num_votes',
            field=models.SmallIntegerField(null=True),
        ),
    ]
