# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0003_answer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_pub_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ask',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
