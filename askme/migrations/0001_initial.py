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
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('titulo', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('asunto', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('fecha_pub', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
                ('respuestas', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(to='askme.Categoria')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('contenido', models.TextField()),
                ('respuesta_fecha_pub', models.DateTimeField(auto_now_add=True)),
                ('votos_respuesta', models.IntegerField(default=0)),
                ('pregunta', models.ForeignKey(to='askme.Pregunta')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
