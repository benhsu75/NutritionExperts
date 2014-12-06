# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
