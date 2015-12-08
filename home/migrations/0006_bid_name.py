# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20151208_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='name',
            field=models.CharField(default=b'Bidder', max_length=32),
        ),
    ]
