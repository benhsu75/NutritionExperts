# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accreditation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField()),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Area_Of_Expertise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email_Signup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expert_Interest_Signup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('experience_text', models.TextField()),
                ('other_text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expert_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('organization', models.CharField(max_length=100, null=True)),
                ('bio', models.TextField(null=True)),
                ('website', models.URLField(null=True)),
                ('image_path', models.CharField(default=b'gray_circle.jpg', max_length=100, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expert_Profile_Accreditation_Rel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accreditation', models.ForeignKey(to='mainapp.Accreditation')),
                ('expert_profile', models.ForeignKey(to='mainapp.Expert_Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expert_Profile_Expertise_Rel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_of_expertise', models.ForeignKey(to='mainapp.Area_Of_Expertise')),
                ('expert_profile', models.ForeignKey(to='mainapp.Expert_Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('five_words', models.CharField(max_length=200, null=True)),
                ('bio', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField()),
                ('text', models.CharField(max_length=500)),
                ('details', models.TextField()),
                ('num_votes', models.SmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sign_Up_Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=100)),
                ('is_expert', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Upvote_Rel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(to='mainapp.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_expert', models.BooleanField(default=False)),
                ('profile_completed', models.BooleanField(default=False)),
                ('expert_profile', models.ForeignKey(null=True, to='mainapp.Expert_Profile', unique=True)),
                ('member_profile', models.ForeignKey(null=True, to='mainapp.Member_Profile', unique=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='upvote_rel',
            name='user_profile',
            field=models.ForeignKey(to='mainapp.User_Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='asked_by_user',
            field=models.ForeignKey(to='mainapp.User_Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='answered_by_user',
            field=models.ForeignKey(to='mainapp.User_Profile'),
            preserve_default=True,
        ),
    ]
