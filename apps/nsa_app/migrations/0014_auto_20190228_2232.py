# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-28 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nsa_app', '0013_auto_20190228_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='nsa_app.City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='profile_pics/defaultprofile.png', upload_to='profile_pics/'),
        ),
    ]