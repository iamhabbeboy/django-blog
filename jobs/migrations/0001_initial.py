# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('datetime', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
