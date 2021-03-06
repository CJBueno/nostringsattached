# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-23 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('when', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/nsa_app/event_photos')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('interests', models.TextField()),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=70)),
                ('photo', models.ImageField(upload_to='media/nsa_app/profile_photos')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='nsa_app.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(related_name='events', to='nsa_app.User'),
        ),
    ]
