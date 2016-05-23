# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20160523_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='end_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'end date'),
        ),
    ]
