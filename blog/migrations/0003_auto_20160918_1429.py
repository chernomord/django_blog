# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='route',
            field=models.CharField(auto_created=True, db_index=True, default='default-title', max_length=40, unique=True),
        ),
    ]
