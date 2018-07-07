# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 08:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180703_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follwers',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='_user_followers_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
