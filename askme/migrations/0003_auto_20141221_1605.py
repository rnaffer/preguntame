# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0002_auto_20141220_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuesta',
            old_name='votos_respuesta',
            new_name='votos',
        ),
    ]
