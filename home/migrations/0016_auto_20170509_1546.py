# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20170509_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='title',
            new_name='name',
        ),
    ]
