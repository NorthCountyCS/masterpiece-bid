# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20160523_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'end date'),
        ),
    ]
