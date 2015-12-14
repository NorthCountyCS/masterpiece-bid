# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_bid_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='artist',
            field=models.CharField(default=b'Anonymous', max_length=32),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='end_date',
            field=models.DateField(verbose_name=b'end date'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='name',
            field=models.CharField(default=b'Anonymous', max_length=32),
        ),
    ]
