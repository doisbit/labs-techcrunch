# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('excerpt', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('author_name', models.CharField(max_length=255)),
                ('author_avatar', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
