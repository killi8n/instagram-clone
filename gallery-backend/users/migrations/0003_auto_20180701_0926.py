# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180701_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='photos/profiles'),
        ),
    ]
