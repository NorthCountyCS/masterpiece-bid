# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to=b'')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name=b'date published')),
                ('end_date', models.DateField(verbose_name=b'date ends')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('bid_date', models.DateField(auto_now_add=True, verbose_name=b'bid date')),
            ],
        ),
        migrations.AddField(
            model_name='artwork',
            name='bidders',
            field=models.ManyToManyField(to='home.Bid'),
        ),
    ]
