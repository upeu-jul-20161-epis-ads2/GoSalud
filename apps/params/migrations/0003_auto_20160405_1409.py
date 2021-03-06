# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0002_remove_person_photo2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='identity_num',
            field=models.CharField(blank=True, error_messages={'unique': 'eeeee ee'}, max_length=20, null=True, verbose_name='Identity num'),
        ),
        migrations.AlterField(
            model_name='person',
            name='identity_type',
            field=models.CharField(choices=[('NID', 'N.I.D.'), ('FC', 'Foreign card'), ('CB', 'Certificate birth'), ('OTHER', 'Other')], default='NID', max_length=10, verbose_name='Identity type'),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, default='persons/default.png', null=True, upload_to='persons', verbose_name='Photo'),
        ),
    ]
