# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-27 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsa_app', '0008_auto_20190226_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to='profile_pics/'),
        ),
    ]
