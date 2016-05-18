# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-18 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belongings', '0011_auto_20160326_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='action',
            field=models.CharField(blank=True, choices=[(b'not_decided', b'Not decided yet'), (b'relocate', b'Relocate'), (b'store', b'Store'), (b'sell', b'Sell'), (b'give', b'Give'), (b'throw_away', b'Throw away')], default='sell', max_length=20, null=True),
        ),
    ]