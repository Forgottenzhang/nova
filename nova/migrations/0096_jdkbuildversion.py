# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-05-17 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0095_auto_20180517_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='JdkBuildVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jdk_version', models.CharField(max_length=20, unique=True, verbose_name='JDK\u7248\u672c')),
                ('app_name', models.CharField(max_length=40, unique=True, verbose_name='\u5e94\u7528\u540d\u79f0')),
                ('env', models.CharField(max_length=40, unique=True, verbose_name='\u5e94\u7528\u90e8\u7f72\u73af\u5883')),
                ('comment', models.CharField(blank=True, max_length=160, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
    ]