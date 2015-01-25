# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_star_rel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('answer', models.ForeignKey(to='mainapp.Answer')),
                ('commented_by_user', models.ForeignKey(to='mainapp.User_Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
