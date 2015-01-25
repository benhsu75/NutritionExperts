# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20141130_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star_Rel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(to='mainapp.Answer')),
                ('user_profile', models.ForeignKey(to='mainapp.User_Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
