# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 15:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20160523_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artist',
            field=models.CharField(default='Anonymous', max_length=32),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='end date(UTC)'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='original_image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='name',
            field=models.CharField(default='Anonymous', max_length=32),
        ),
        migrations.AddField(
            model_name='artwork',
            name='auction',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Auction'),
        ),
    ]
