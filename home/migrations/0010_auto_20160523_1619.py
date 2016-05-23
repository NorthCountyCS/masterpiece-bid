# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20160523_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 23, 16, 19, 32, 425304), verbose_name=b'end date'),
        ),
    ]
