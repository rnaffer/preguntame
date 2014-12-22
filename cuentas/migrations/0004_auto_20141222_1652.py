# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_datosusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosusuario',
            name='reputacion',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
