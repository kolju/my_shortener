# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0003_auto_20160712_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='id',
        ),
        migrations.AlterField(
            model_name='link',
            name='short',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
