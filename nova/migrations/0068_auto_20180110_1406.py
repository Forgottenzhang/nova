# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-10 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0067_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='\u8bf4\u660e'),
        ),
        migrations.AlterField(
            model_name='config',
            name='config_value',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='\u914d\u7f6e\u53c2\u6570\u503c'),
        ),
    ]
