# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20150107_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='profile_image',
            field=models.ImageField(upload_to=accounts.models.get_image_path, default='/static/img/profile.png'),
            preserve_default=True,
        ),
    ]
