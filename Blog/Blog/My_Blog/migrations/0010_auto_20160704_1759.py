# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-04 14:59
from __future__ import unicode_literals

import Blog.My_Blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Blog', '0009_auto_20160704_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Blog.My_Blog.models.content_file_name),
        ),
    ]
