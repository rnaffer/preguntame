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
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('answer_pub_date', models.DateTimeField()),
                ('votes', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length='255')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('popularity', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length='255')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length='255')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ask',
            name='category',
            field=models.ForeignKey(to='askme.Category', related_name='category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ask',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='asks'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='ask',
            unique_together=set([('user', 'issue')]),
        ),
        migrations.AddField(
            model_name='answer',
            name='ask',
            field=models.ForeignKey(to='askme.Ask', related_name='answers'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('ask', 'content')]),
        ),
    ]
