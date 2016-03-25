# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20160325_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='storage_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='boxes', to='common.StoragePlace'),
        ),
        migrations.AlterField(
            model_name='item',
            name='box',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='common.Box'),
        ),
        migrations.AlterField(
            model_name='item',
            name='receiver',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='free_items', to='common.Receiver'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sale',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item', to='common.Sale'),
        ),
        migrations.AlterField(
            model_name='item',
            name='storage_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='common.StoragePlace'),
        ),
        migrations.AlterField(
            model_name='receiver',
            name='preferred_contact_channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.ContactChannel'),
        ),
    ]
