# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_userdetail_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='profile_image',
            field=models.ImageField(null=True, blank=True, upload_to=accounts.models.get_image_path),
            preserve_default=True,
        ),
    ]
