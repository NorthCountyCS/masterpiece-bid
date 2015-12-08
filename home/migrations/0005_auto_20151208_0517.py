# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20151207_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to=b'static/images'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='original_image',
            field=models.ImageField(upload_to=b'static/images', blank=True),
        ),
    ]
