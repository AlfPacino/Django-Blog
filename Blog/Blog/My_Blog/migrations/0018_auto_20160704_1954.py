# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-04 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Blog', '0017_auto_20160704_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/Posts_Images'),
        ),
    ]
