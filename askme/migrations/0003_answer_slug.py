# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0002_remove_answer_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='slug',
            field=models.SlugField(blank=True, max_length='255', default=''),
            preserve_default=True,
        ),
    ]
