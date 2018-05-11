# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-16 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0088_auto_20180316_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appgroup',
            name='comment',
            field=models.CharField(blank=True, max_length=160, null=True, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='appgroup',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name='\u5e94\u7528\u7ec4\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='env',
            field=models.CharField(blank=True, choices=[(b'product', '\u751f\u4ea7\u73af\u5883'), (b'staging', '\u51c6\u751f\u4ea7\u73af\u5883'), (b'test', '\u6d4b\u8bd5\u73af\u5883'), (b'dev', '\u5f00\u53d1\u73af\u5883')], max_length=128, null=True, verbose_name='\u8fd0\u884c\u73af\u5883'),
        ),
    ]