# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belongings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='action',
            field=models.CharField(blank=True, choices=[(b'not_decided', b'Not decided yet'), (b'relocate', b'Relocate'), (b'store', b'Store'), (b'sell', b'Sell'), (b'give', b'Give')], default='sell', max_length=20, null=True),
        ),
    ]