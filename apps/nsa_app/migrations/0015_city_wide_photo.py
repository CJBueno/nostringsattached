# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-28 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsa_app', '0014_auto_20190228_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='wide_photo',
            field=models.ImageField(default='city_photos/wide_san_fran.jpg', upload_to='city_photos/'),
            preserve_default=False,
        ),
    ]
