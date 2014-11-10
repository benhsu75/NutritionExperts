# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_signup',
            name='email',
            field=models.CharField(max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
