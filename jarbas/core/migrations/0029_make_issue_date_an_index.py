# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20170601_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreimbursement',
            name='issue_date',
            field=models.DateField(db_index=True, verbose_name='Data de Emissão'),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='issue_date',
            field=models.DateField(db_index=True, verbose_name='Data de Emissão'),
        ),
    ]
