# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-04 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Blog', '0016_auto_20160704_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/app/images'),
        ),
    ]