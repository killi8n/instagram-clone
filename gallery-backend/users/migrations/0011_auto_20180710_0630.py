# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-10 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180710_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='photos/profiles/no_image.png', null=True, upload_to='photos/profiles'),
        ),
    ]
