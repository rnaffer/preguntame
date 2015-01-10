# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0005_answer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerVoteUsers',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(max_length=150)),
                ('answer', models.ForeignKey(to='askme.Answer', related_name='users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='ask',
            name='category',
            field=models.ForeignKey(to='askme.Category', related_name='asks'),
            preserve_default=True,
        ),
    ]
