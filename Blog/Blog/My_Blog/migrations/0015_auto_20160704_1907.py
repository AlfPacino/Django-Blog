# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-04 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Blog', '0014_auto_20160704_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='C:\\Users\\Dex\\Desktop\\Blog\\Blog\\Blog\\My_Blog\\Images'),
        ),
    ]