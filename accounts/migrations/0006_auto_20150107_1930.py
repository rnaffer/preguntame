# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userdetail_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='about_me',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(default='user@email.com', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='first_name',
            field=models.CharField(default='user_name', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='last_name',
            field=models.CharField(default='user_name', max_length=50),
            preserve_default=True,
        ),
    ]
