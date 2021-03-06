# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0018_auto_20170807_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='creation_date',
            field=models.IntegerField(help_text='Enter a year in YYYY format, like 1978 or 2017', null=True),
        ),
        migrations.AlterField(
            model_name='artworkimage',
            name='image',
            field=models.ImageField(help_text='Image file upload size limit is 2.5MB.', upload_to='artworks/'),
        ),
        migrations.AlterField(
            model_name='artworkimage',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
