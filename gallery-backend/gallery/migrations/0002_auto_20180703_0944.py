# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='photos/no_image.png', null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
