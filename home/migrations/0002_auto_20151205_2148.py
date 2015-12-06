# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='bidders',
        ),
        migrations.AddField(
            model_name='bid',
            name='artwork',
            field=models.ForeignKey(default=0, to='home.Artwork'),
            preserve_default=False,
        ),
    ]
